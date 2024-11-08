<h1>Automotive Night Vision</h1>
<hr><p>This project was created with comfort, versatility and affordability in mind. It's intended to use existing infrastrucutre, by switching composite video signal from rear-view camera feed to intended present thermal images. Night vision set consists of thermal camera, 3D printed housing, adapters and computer of choice.</p><h2>Technologies Used</h2>
<hr><ul>
<li>Python</li>
</ul><ul>
<li>OpenCV</li>
</ul><ul>
<li>Ultralytics</li>
</ul><ul>
<li>YOLO</li>
</ul><h2>Setup</h2>
<hr><p>Project needs to run on python 3.8+, other requirements for the project are listed in requirements.txt</p><h2>Usage</h2>
<hr><p>To simply display the thermal camera feed without object detection, run:</p>
<p>python camera.py</p>
<p>This application will open a window showing the thermal image in real-time.</p>
<hr>
<p>To enable object detection on the thermal feed, run:</p>
<p>python yolo-object-detection.py</p>
<p>This will display the thermal camera feed with bounding boxes around detected objects. The YOLOv10 model from the Ultralytics library will be used to perform real-time detection of the Xinfrared XH-09 feed.</p><h2>Project Status</h2>
<hr><p>In Progres</p><h2>Improvements</h2>
<hr><ul>
<li>improve quality and speed of detection</li>
</ul><ul>
<li>Create a model based on own data</li>
</ul><ul>
<li>Redesign case</li>
</ul><h2>Features that can be added</h2>
<hr><ul>
<li>Apply SAM2 detection</li>
</ul><ul>
<li>Sound notification</li>
</ul><h2>Contact</h2>
<hr><p><span style="margin-right: 30px;"></span><a href="https://www.linkedin.com/in/jakub-kotecki/"><img target="_blank" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" style="width: 10%;"></a><span style="margin-right: 30px;"></span><a href="https://github.com/jakubkotecki6"><img target="_blank" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" style="width: 10%;"></a></p>
