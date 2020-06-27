# MUnet-LUC
Land Use Classification with mUnet by <a href = "https://github.com/abhi170599">Abhishek </a> and <a href="https://github.com/sayonpalit">Sayon</a>
<h2>Description</h2>
<p>We aimed at developing a deep learning Pipeline to classify land use types from satellite images.<br>
        Land Use can be classified into following classes-<br>
        <ol>
            <li>Buildings</li>
            <li>Trees</li>
            <li>Crops</li>
            <li>Roads & Tracks</li>
            <li>Water</li>
            <li>Empty Fields</li>
        </ol>
</p>
<h2>Model Overview</h2>
<p>We used the <a href= "http://www.insticc.org/Primoris/Resources/PaperPdf.ashx?idPaper=73706">paper </a>by Lakshya Garg et al
to implement their proposed Modified UNet Architecture for Land Use Classification of Satellite Imagery</p>
<br>
<h3>Modified UNet Architecture</h2>
<img src="https://raw.githubusercontent.com/abhi170599/MUnet-LUC/698627329b6f68000861a1140a680f225e415baa/Screen%20Shot%202020-05-20%20at%205.05.49%20PM.png" border = "5">

<h2>Results and Inference</h2>
<img src = "https://github.com/abhi170599/MUnet-LUC/blob/master/Screen%20Shot%202020-05-19%20at%208.55.34%20PM.png">
<img src = "https://github.com/abhi170599/MUnet-LUC/blob/master/Screen%20Shot%202020-05-19%20at%208.53.52%20PM.png">
<p>Model was trained on <a href = "colab.research.google.com"> Colab's</a> <b>12GB NVIDIA Tesla K80 GPU</b> for 150 epochs <br>
with training accuracy of 80.037%</p>
<img src = "https://github.com/abhi170599/MUnet-LUC/blob/master/Screen%20Shot%202020-05-20%20at%208.09.30%20AM.png">
<table>
<tr>
<th>Model</th>
<th>$Parameters</th>
<th>Accuracy</th>
</tr>
<tr>
<td>AlexNet</td>
<td>61,000,000</td>
<td>78.234%</td>
</tr>
<tr>
<td>UNet</td>
<td>31,379,205</td>
<td>62.1077%</td>
</tr>
<tr>
<td>mUnet</td>
<td>31,105,669</td>
<td>80.897%</td>
</tr>
</table>
<h2>Applications</h2>
<li>Smart City Planning (Searching Construction Space, Monitoring Vegetation etc.)</li>
<li>Defence Applications</li>
<li>Natural Resource Monitoring and Management ✓Disaster Management</li> 
