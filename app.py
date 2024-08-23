from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
    {
        'id': 1,
        'title': 'Sidewalk Segmentation, Refinement, and Route Optimization',
        'keywords': 'Deep Learning, Semantic Segmentation, Segmentation Refinement, Route Optimization',
        'description': 'Master\'s thesis: This thesis presents a comprehensive approach to sidewalk extraction and refinement using deep learning techniques, focusing on semantic segmentation methods. The research explores the challenges of accurately identifying and delineating sidewalks from complex urban environments. The proposed method utilizes advanced segmentation models to extract sidewalks from high-resolution imagery, followed by refinement processes to enhance the accuracy and usability of the extracted data.In addition to sidewalk extraction, the thesis addresses the problem of route optimization on the extracted sidewalks. A novel approach based on the mini-max function is introduced to optimize pedestrian paths, aiming to minimize the maximum distance or cost in the route. This approach is particularly beneficial for ensuring efficient and safe navigation in urban areas, where sidewalk conditions can vary significantly.The findings of this research contribute to the development of smarter urban planning tools and autonomous navigation systems, offering a robust solution for both public and commercial applications.',
        'link': 'https://github.com/WillBao33/Masters_Thesis'
    },
    {
        'id':2,
        'title':'Autonomous Delivery Robot',
        'keywords':'Autonomous Driving, Sensor Fusion, Path Planning',
        'description': 'An autonomous delivery robot utilized RTK-GPS, Velodyne lidar, and IMU sensors for precise localization, and combined camera and lidar data for real-time object detection and classification. Advanced path-planning algorithms, including Pure Pursuit and Model Predictive Controllers, enabled the robot to autonomously plan routes and avoid obstacles. This project demonstrated the integration of multiple cutting-edge technologies to achieve reliable autonomous navigation in complex settings.',
        'link': 'https://youtu.be/cXYToMjpoJQ'
    },
    {
        'id': 3,
        'title': 'Food Classifier',
        'keywords': 'Deep Learning, Vision Transformer, Object Recognition',
        'description': 'This project involves the implementation of a Vision Transformer (ViT) model from scratch, designed to classify images from the Food101 dataset. The Food101 dataset contains over 100,000 images of food items, categorized into 101 different classes. By leveraging the power of transformers, which have been highly effective in natural language processing, this project explores their application in computer vision tasks. The ViT model was constructed without relying on any pre-built libraries for transformers, ensuring a deep understanding of the architecture and its underlying mechanics. After successful implementation, the model was trained on the Food101 dataset, demonstrating impressive performance in image classification tasks. Upon achieving satisfactory results, the trained model was deployed on Hugging Face, making it accessible for inference and further experimentation by the community. This project not only highlights the potential of transformers in visual recognition but also provides a valuable resource for researchers and developers interested in the application of deep learning models in diverse domains.',
        'link': 'https://huggingface.co/spaces/WillBao/Food101_ViT'
    },
    {
        'id': 4,
        'title': 'Google Data Analytic Certificate Bellabeat Case Study',
        'keywords': 'Data Analysis, Health Metrics, User Behavior, Smart Devices',
        'description': 'This project involves a comprehensive data analysis case study on Bellabeat, a high-tech company that manufactures health-focused smart devices for women. The primary objective of this study was to analyze user data from Bellabeat devices to uncover patterns and trends in health and wellness metrics, with a particular focus on understanding user behavior. Using various data analytics techniques, we explored key metrics such as physical activity, sleep patterns, and heart rate to identify correlations and provide actionable insights. The analysis helped in understanding how users interact with Bellabeat devices and highlighted areas for potential product improvement and feature enhancement. The findings from this study are intended to assist Bellabeat in refining their product offerings, enhancing user engagement, and optimizing the overall user experience. This project demonstrates the power of data-driven decision-making in developing innovative solutions in the wearable technology and health monitoring space.',
        'link': 'https://github.com/WillBao33/Bellabeat_case_study'
    },
    {
        'id': 5,
        'title': 'Automated Weld Inspection Using Industrial Robots and Computer Vision',
        'keywords': 'Weld Inspection, Computer Vision, Trajectory Planning, Automation',
        'description': 'This project involved the development of an automated weld inspection system at Bluewrist Inc., leveraging industrial robots and computer vision technology. The primary goal was to enhance the accuracy and efficiency of weld quality inspection processes in industrial settings. As part of this project, I contributed to the mechanical design and programming of robotic systems, specifically utilizing UR10 robot. The robot was programmed to perform precise, repeatable movements for inspecting welds on various components. By integrating advanced computer vision techniques, the system was capable of identifying and assessing weld quality, detecting defects such as cracks, porosity, and incomplete fusion. The automated solution significantly reduced the need for manual inspection, thereby improving productivity and ensuring consistent quality control. This project highlights the potential of robotics and computer vision in automating complex inspection tasks, providing reliable and scalable solutions for manufacturing environments.',
        'link': 'https://youtu.be/Mtrd7-1e9eA'
    },
]


@app.route("/")
def hello():
  return render_template('home.html', projects=PROJECTS)


@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
