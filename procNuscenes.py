import os
import lanelet2
from lanelet2.core import (Lanelet, LaneletMap)
from lanelet2.projection import (LocalCartesianProjector)
import lanelet2.traffic_rules
import scipy.io as sio

class procNuScenes :
    def __init__(self,file_path,org):
        self.projector = LocalCartesianProjector(lanelet2.io.Origin(org[0], org[1]))
        self.path = file_path
        self.map = lanelet2.io.load(self.path,self.projector)
    def process(self):
        traffic_rules = lanelet2.traffic_rules.create(lanelet2.traffic_rules.Locations.Germany,
                                                      lanelet2.traffic_rules.Participants.Vehicle)
        graph = lanelet2.routing.RoutingGraph(self.map, traffic_rules)
        edges = []
        llt_id_lst = []
        ls_pts = []
        ls_ids = []
        ls_frontNode_ids = []
        ls_backNode_ids = []

        for llt in self.map.laneletLayer:
            llt_id_lst.append(llt.id)
            next = graph.following(llt)
            left = [[p.x, p.y, p.z] for p in llt.leftBound]
            right = [[p.x, p.y, p.z] for p in llt.rightBound]
            ls_ids.append(llt.leftBound.id)
            ls_ids.append(llt.rightBound.id)
            ls_pts.append(left)
            ls_pts.append(right)
            ls_frontNode_ids.append(llt.leftBound[0].id)
            ls_frontNode_ids.append(llt.rightBound[0].id)
            ls_backNode_ids.append(llt.leftBound[-1].id)
            ls_backNode_ids.append(llt.rightBound[-1].id)
            for next_llt in next:
                edges.append((llt.leftBound.id, next_llt.leftBound.id))
                edges.append((llt.rightBound.id, next_llt.rightBound.id))
                ls_ids.append(next_llt.leftBound.id)
                ls_ids.append(next_llt.rightBound.id)
                next_left = [[p.x, p.y, p.z] for p in next_llt.leftBound]
                next_right = [[p.x, p.y, p.z] for p in next_llt.rightBound]
                ls_pts.append(next_left)
                ls_pts.append(next_right)

                ls_frontNode_ids.append(next_llt.leftBound[0].id)
                ls_frontNode_ids.append(next_llt.rightBound[0].id)
                ls_backNode_ids.append(next_llt.leftBound[-1].id)
                ls_backNode_ids.append(next_llt.rightBound[-1].id)
        
        path_lst_ids = self.path.split("/")
        path_lst_pts = self.path.split("/")
        path_lst_edges = self.path.split("/")
        path_lst_frontNodeIds = self.path.split("/")
        path_lst_backNodeIds = self.path.split("/")

        last_el_ids = path_lst_ids[-1][0:-4] + "-ids.mat"
        last_el_pts = path_lst_pts[-1][0:-4] + "-pts.mat"
        last_el_edges = path_lst_edges[-1][0:-4] + "-edges.mat"
        last_el_frontNodeIds = path_lst_frontNodeIds[-1][0:-4] + "-frontIds.mat"
        last_el_backNodeIds = path_lst_backNodeIds[-1][0:-4] + "-backIds.mat"

        path_lst_ids[-1] = last_el_ids
        path_lst_pts[-1] = last_el_pts
        path_lst_edges[-1] = last_el_edges
        path_lst_frontNodeIds[-1] = last_el_frontNodeIds
        path_lst_backNodeIds[-1] = last_el_backNodeIds

        save_path_ids = '/'.join(path_lst_ids)
        save_path_pts = '/'.join(path_lst_pts)
        save_path_edges = '/'.join(path_lst_edges)
        save_path_frontNodeIds = '/'.join(path_lst_frontNodeIds)
        save_path_backNodeIds = '/'.join(path_lst_backNodeIds)

        sio.savemat(save_path_ids,{'ls_ids': ls_ids},oned_as='row')
        sio.savemat(save_path_pts,{'ls_pts': ls_pts},oned_as='row')
        sio.savemat(save_path_edges,{'edges': edges},oned_as='row')
        sio.savemat(save_path_frontNodeIds,{'ls_frontNode_ids': ls_frontNode_ids},oned_as='row')
        sio.savemat(save_path_backNodeIds,{'ls_backNode_ids': ls_backNode_ids},oned_as='row')

if __name__ == '__main__':
    org = (42.34,-71.03)
    proc = procNuScenes("Data/nuScenes2Lanelet/boston-seaport.osm",org)
    # org = (1.32,103.79)
    # proc = procNuScenes("Data/nuScenes2Lanelet/singapore-hollandvillage.osm",org)
    # proc = procNuScenes("Data/nuScenes2Lanelet/singapore-onenorth.osm",org)
    # proc = procNuScenes("Data/nuScenes2Lanelet/singapore-queenstown.osm",org)
    proc.process()