# Efficient Arc Spline Approximation
Efficient Arc Spline Approximation of Large Scale Complex Lane-Level Road Maps
* Install MATLAB and open figures to view the arc spline approximation results for each map dataset.

* Lanelet maps converted from nuScenes dataset are from the work of Naumann et al. (2023)

* To run python script, install lanelet2.

# Example Results 
To accurately view the arc spline approximation results, download the interactive .fig files and open with MATLAB. The pdf files only show the overall result in a low resolution.

* [Boston Seaport](/fig_boston.pdf?raw=true)

* [Singapore One North](https://github.com/user-attachments/files/18406135/fig_onenorth.pdf)

* [Singapore Holland Village](https://github.com/user-attachments/files/18406138/fig_hollandvillage.pdf)

* [Singapore Queenstown](https://github.com/user-attachments/files/18406137/fig_queenstown.pdf)

## References
If you are using our work in your study, please cite our [papers](https://www.sciencedirect.com/science/article/pii/S0167839624000979)
```
@article{Jeon2024_2
title = {Efficient Arc Spline Approximation of Large Scale Complex Lane-Level Road Maps},
journal = {**},
volume = {**},
pages = {**},
year = {2024},
issn = {**},
doi =  {**},
url = {**},
keywords = {**},
abstract = {**}
}

@article{Jeon2024_1,
title = {Reliability-based {G}1 continuous arc spline approximation},
journal = {Computer Aided Geometric Design},
volume = {112},
pages = {102363},
year = {2024},
issn = {0167-8396},
doi = {https://doi.org/10.1016/j.cagd.2024.102363},
url = {https://www.sciencedirect.com/science/article/pii/S0167839624000979},
author = {Jinhwan Jeon and Yoonjin Hwang and Seibum B. Choi},
keywords = {Reliability, Arc splines,  continuity, Constrained nonlinear least squares, Optimization},
abstract = {This paper introduces an algorithm for approximating a set of data points with G1 continuous arcs, leveraging covariance data associated with the points. Prior approaches to arc spline approximation typically assumed equal contribution from all data points, resulting in potential algorithmic instability when outliers are present. To address this challenge, we propose a robust method for arc spline approximation, taking into account the 2D covariance of each data point. Beginning with the definition of models and parameters for single-arc approximation, we extend the framework to support multiple-arc approximation for broader applicability. Finally, we validate the proposed algorithm using both synthetic noisy data and real-world data collected through vehicle experiments conducted in Sejong City, South Korea.}
}
```

and the following paper of [Lanelet2 for nuScenes](https://openaccess.thecvf.com/content/CVPR2023W/E2EAD/html/Naumann_Lanelet2_for_nuScenes_Enabling_Spatial_Semantic_Relationships_and_Diverse_Map-Based_CVPRW_2023_paper.html)

```
@InProceedings{Naumann2023,
author    = {Naumann, Alexander and Hertlein, Felix and Grimm, Daniel and Zipfl, Maximilian and Thoma, Steffen and Rettinger, Achim and Halilaj, Lavdim and Luettin, Juergen and Schmid, Stefan and Caesar, Holger},
title     = {Lanelet2 for nuScenes: Enabling Spatial Semantic Relationships and Diverse Map-Based Anchor Paths},
booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
month     = {June},
year      = {2023},
pages     = {3247-3256}
}
```
