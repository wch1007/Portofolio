import streamlit as st
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Projects | Chenghao Wang - Portfolio",
    page_icon="🚀",
    layout="wide",
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        .main {
            padding: 2rem 2rem;
        }
        h1, h2, h3 {
            font-family: 'Helvetica', sans-serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .section-header {
            color: #1E3A8A;
            border-bottom: 2px solid #1E3A8A;
            padding-bottom: 0.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .project-card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .skill-tag {
            background-color: #E2E8F0;
            padding: 4px 8px;
            border-radius: 15px;
            font-size: 0.85rem;
            color: #1E3A8A;
            display: inline-flex;
            margin-right: 4px;
            margin-bottom: 4px;
            white-space: nowrap;
        }
        .skills-container {
            margin-top: 8px;
            margin-bottom: 15px;
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            max-width: 100%;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
        }
        .stTabs [data-baseweb="tab"] {
            height: 4rem;
            white-space: pre-wrap;
            font-size: 1rem;
            font-weight: 600;
            color: #1E3A8A;
        }
        .directory-card {
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            background-color: #f8f9fa;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .directory-item {
            padding: 10px;
            margin-bottom: 5px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .directory-item:hover {
            background-color: #E2E8F0;
            cursor: pointer;
        }
        .directory-title {
            font-weight: 600;
            color: #1E3A8A;
            margin-bottom: 5px;
        }
        .directory-description {
            font-size: 0.9rem;
            color: #4B5563;
        }
        .category-section {
            margin-top: 30px;
            padding-top: 30px;
            border-top: 1px solid #E2E8F0;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Page header
st.markdown('<h1 class="section-header">My Projects</h1>', unsafe_allow_html=True)
st.write("Here are some of the key projects I've worked on. Each demonstrates my technical skills and problem-solving abilities.")

# Project categories tabs
project_tabs = st.tabs([
    "Robotics Projects", 
    "Research Projects", 
    "Software Development", 
    "Data Science"
])

# Tab 1: Robotics Projects
with project_tabs[0]:
    # Directory section
    st.markdown('<div class="directory-card">', unsafe_allow_html=True)
    st.markdown("### Directory")
    st.markdown("Navigate to specific projects:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Project 1 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('desktop-robot').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Desktop Companion Robot</div>
                <div class="directory-description">An interactive desktop robot with social capabilities designed for daily assistance and companionship.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 2 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('robot-arm').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">6-DOF Robot Arm</div>
                <div class="directory-description">A versatile robotic arm designed for precise manipulation tasks in educational settings.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        # Project 3 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('autonomous-vehicle').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Autonomous Navigation System</div>
                <div class="directory-description">A navigation system for small-scale autonomous vehicles using ROS and computer vision.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 4 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('drone-project').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Aerial Drone Project</div>
                <div class="directory-description">A custom drone platform with environmental sensing capabilities for urban monitoring.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown('<div id="desktop-robot" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Desktop Companion Robot")
    st.markdown("**Duration:** September 2023 - Present")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/cute-robot-holding-phone-cartoon-vector-icon-illustration-science-technology-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-3717.jpg", caption="Desktop Robot Prototype")
    
    with col2:
        st.markdown("""
        ### Overview
        As Product Director at Tangwen Zhixin Technology, I led the development of an interactive desktop companion robot with social capabilities designed to provide assistance, entertainment, and companionship.
        
        ### Challenge
        Creating a robot that could both understand human intentions and respond with appropriate social cues while maintaining an affordable price point for consumer markets.
        
        ### Solution
        We developed a compact desktop robot with:
        - Natural language processing capabilities for human-robot communication
        - Computer vision systems for user recognition and basic object detection
        - Expressive movement patterns to convey emotion and intent
        - Cloud-connected intelligence with on-device processing for privacy
        
        ### Key Contributions
        - Developed the product roadmap and technical specifications
        - Created interaction design protocols for natural human-robot interactions
        - Led a team of 5 engineers in implementing the prototype
        - Secured $300,000 in seed funding from MiraclePlus
        - Showcased the prototype at the China International High-tech Expo (CHITEC)
        
        ### Results
        - Successfully developed a working prototype within 8 months
        - Received positive feedback from potential customers in early demonstrations
        - Established the foundation for product expansion and market validation
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Python", "ROS2", "Arduino", "Machine Learning", "Computer Vision", "NLP", "3D Printing", "Fusion 360"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 2
    st.markdown('<div id="robot-arm" class="project-card">', unsafe_allow_html=True)
    st.markdown("## 6-DOF Robot Arm")
    st.markdown("**Duration:** May 2023 - December 2023")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/premium-photo/robot-arm-industrial-white-background_36367-76.jpg", caption="Robot Arm Prototype")
    
    with col2:
        st.markdown("""
        ### Overview
        Designed and built a 6-degree of freedom robotic arm for educational purposes at Tsinghua University, enabling students to learn about inverse kinematics and robotic control.
        
        ### Challenge
        Creating an affordable yet precise robotic arm that could serve as a learning platform while maintaining sufficient payload capacity for practical demonstrations.
        
        ### Solution
        Developed a modular design with:
        - 6 servo motors with varying torque capabilities
        - 3D printed structural components for cost-effective customization
        - Custom control PCB with Arduino integration
        - ROS-based software for programming and control
        
        ### Key Contributions
        - Designed the mechanical structure and joints
        - Engineered the control systems and electronic interfaces
        - Developed educational materials and exercises
        - Created a calibration system for high precision
        
        ### Results
        - Achieved 0.5mm positioning accuracy
        - Successfully implemented in undergraduate robotics courses
        - Used by 3 research groups for various manipulation experiments
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["ROS", "C++", "Arduino", "CAD", "3D Printing", "PCB Design", "Servo Control", "Inverse Kinematics"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 3
    st.markdown('<div id="autonomous-vehicle" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Autonomous Navigation System")
    st.markdown("**Duration:** January 2022 - June 2022")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/autonomous-car-concept-illustration_114360-8447.jpg", caption="Navigation System")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed an autonomous navigation system for small-scale vehicles, combining computer vision with sensor fusion to navigate indoor environments.
        
        ### Challenge
        Creating a reliable navigation system that could operate without GPS in indoor environments while avoiding obstacles and following designated paths.
        
        ### Solution
        Implemented a system featuring:
        - LiDAR-based SLAM for mapping and localization
        - Computer vision for lane detection and object recognition
        - Sensor fusion algorithm combining data from multiple sensors
        - Path planning and obstacle avoidance algorithms
        
        ### Key Contributions
        - Developed the sensor fusion architecture
        - Implemented computer vision algorithms for feature detection
        - Created the obstacle avoidance system
        - Optimized the navigation algorithms for resource-constrained hardware
        
        ### Results
        - Successfully navigated complex indoor courses with 95% accuracy
        - Demonstrated at a university technology showcase
        - Published navigation algorithms as open-source resources
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["ROS", "Python", "Computer Vision", "SLAM", "Sensor Fusion", "Path Planning", "Raspberry Pi", "LiDAR"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 4
    st.markdown('<div id="drone-project" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Aerial Drone Project")
    st.markdown("**Duration:** April 2021 - November 2021")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/drone-realistic-composition-with-flying-quadcopter-executing-command-vector-illustration_1284-66163.jpg", caption="Drone Project")
    
    with col2:
        st.markdown("""
        ### Overview
        Built a custom quadcopter drone equipped with environmental sensors for urban air quality monitoring and data collection.
        
        ### Challenge
        Developing a stable aerial platform that could carry environmental sensors while maintaining sufficient flight time and data transmission capabilities.
        
        ### Solution
        Created a custom drone with:
        - Lightweight carbon fiber frame for maximum payload capacity
        - Optimized battery and power management system
        - Environmental sensor array (PM2.5, CO2, temperature, humidity)
        - Real-time data transmission and mapping capabilities
        
        ### Key Contributions
        - Designed the drone's structural and electronic systems
        - Integrated the environmental sensor package
        - Developed the data collection and transmission software
        - Created visualization tools for the collected environmental data
        
        ### Results
        - Achieved 25-minute flight time with full sensor package
        - Successfully mapped air quality variations across campus
        - Data collected contributed to a university environmental study
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Drone Design", "Arduino", "Environmental Sensors", "Data Visualization", "Wireless Communication", "Flight Control", "CAD", "3D Printing"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: Research Projects
with project_tabs[1]:
    # Directory section
    st.markdown('<div class="directory-card">', unsafe_allow_html=True)
    st.markdown("### Directory")
    st.markdown("Navigate to specific projects:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Project 1 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('hri-research').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Human-Robot Interaction Research</div>
                <div class="directory-description">Research on natural interaction patterns between humans and social robots, published at HRI'2024.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 2 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('ml-gesture').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Machine Learning for Gesture Recognition</div>
                <div class="directory-description">Research on using deep learning to recognize and interpret human gestures for robot control.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        # Project 3 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('vr-simulation').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">VR Simulation for Robot Training</div>
                <div class="directory-description">Using virtual reality environments to train robotic systems before real-world deployment.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 4 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('architecture-ai').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">AI in Architectural Design</div>
                <div class="directory-description">Applying machine learning to architectural design problems for space optimization.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 1: HRI Research
    st.markdown('<div id="hri-research" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Human-Robot Interaction Research")
    st.markdown("**Duration:** January 2023 - June 2024")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/artificial-intelligence-concept-with-human-head-outline_23-2147850167.jpg", caption="HRI Research")
    
    with col2:
        st.markdown("""
        ### Overview
        Conducted research on natural interaction patterns between humans and social robots at Tsinghua University's Pervasive HCI Lab, resulting in a Late-Breaking Report published at the HRI'2024 conference.
        
        ### Research Question
        How can we design robot behaviors that feel natural and intuitive to human users without requiring explicit training or instruction?
        
        ### Methodology
        - Conducted user studies with 30+ participants of varying ages and technological familiarity
        - Used mixed-methods approach combining qualitative observations and quantitative metrics
        - Developed and tested multiple interaction prototypes with varying degrees of social expressivity
        - Analyzed data using statistical methods to identify significant patterns
        
        ### Key Contributions
        - Designed and conducted comprehensive user studies
        - Developed novel interaction frameworks based on human social psychology
        - Analyzed interaction data using rigorous statistical methods
        - Published findings in a peer-reviewed conference (HRI'2024)
        - Presented research to academic and industry audiences
        
        ### Results
        - Identified key behavioral patterns that significantly improved human-robot interaction quality
        - Demonstrated that subtle non-verbal cues can substantially enhance perceived robot intelligence
        - Created design guidelines for robot behavior that have been incorporated into our company's product development
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies and Methods used:**")
        skills = ["Python", "R", "Statistical Analysis", "Qualitative Research", "User Studies", "Prototype Development", "Literature Review"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional research projects in the Research tab:
    # Project 2: ML Gesture
    st.markdown('<div id="ml-gesture" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Machine Learning for Gesture Recognition")
    st.markdown("**Duration:** May 2022 - December 2022")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/gesture-recognition-abstract-concept-illustration_335657-3822.jpg", caption="Gesture Recognition")
    
    with col2:
        st.markdown("""
        ### Overview
        Researched and developed machine learning models for recognizing human gestures to enable more intuitive robot control interfaces.
        
        ### Research Question
        How can machine learning models effectively recognize complex hand gestures in real-time with sufficient accuracy for robot control applications?
        
        ### Methodology
        - Collected a dataset of 5,000+ gesture samples from 25 participants
        - Implemented several deep learning architectures (CNN, LSTM, Transformer)
        - Developed real-time processing pipeline with optimization for edge computing
        - Conducted comparative analysis of model performance across different metrics
        
        ### Key Contributions
        - Created a novel hybrid CNN-LSTM architecture optimized for gesture recognition
        - Developed data augmentation techniques for improved model generalization
        - Implemented real-time inference on resource-constrained platforms
        - Open-sourced the gesture dataset and baseline models
        
        ### Results
        - Achieved 94% accuracy in real-time gesture recognition
        - Reduced inference time to 15ms on embedded platforms
        - Successfully integrated with robot control systems for demonstration
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies and Methods used:**")
        skills = ["PyTorch", "TensorFlow", "Computer Vision", "Deep Learning", "Data Collection", "Real-time Processing", "Edge AI", "Model Optimization"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 3: VR Simulation
    st.markdown('<div id="vr-simulation" class="project-card">', unsafe_allow_html=True)
    st.markdown("## VR Simulation for Robot Training")
    st.markdown("**Duration:** September 2022 - April 2023")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/virtual-reality-concept-illustration_114360-2077.jpg", caption="VR Simulation")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed a virtual reality environment for training and testing robotic systems before deployment in real-world settings.
        
        ### Research Question
        Can VR simulations effectively bridge the reality gap to enable more efficient robot training and reduce physical prototyping time?
        
        ### Methodology
        - Created high-fidelity VR environments mimicking target deployment scenarios
        - Implemented physics-based simulation with accurate robot kinematics
        - Developed domain randomization techniques for robustness
        - Conducted comparative studies between VR-trained and traditionally-trained robots
        
        ### Key Contributions
        - Designed the VR environment and simulation framework
        - Implemented domain randomization techniques for sim-to-real transfer
        - Created a library of challenging scenarios for robot testing
        - Developed metrics for evaluating simulation fidelity
        
        ### Results
        - Reduced physical robot training time by 60%
        - Improved robot performance on novel tasks by 40%
        - Successfully transferred learned policies from simulation to real robots
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies and Methods used:**")
        skills = ["Unity3D", "C#", "VR Development", "Physics Simulation", "Robot Simulation", "Domain Randomization", "Reinforcement Learning", "Sim-to-Real Transfer"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 4: Architecture AI
    st.markdown('<div id="architecture-ai" class="project-card">', unsafe_allow_html=True)
    st.markdown("## AI in Architectural Design")
    st.markdown("**Duration:** January 2021 - June 2021")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/futuristic-architecture-blue-background-with-white-building-design_53876-119505.jpg", caption="Architecture AI")
    
    with col2:
        st.markdown("""
        ### Overview
        Applied machine learning techniques to architectural design problems, focusing on space optimization and workflow efficiency in building layouts.
        
        ### Research Question
        How can AI systems assist architects in optimizing spatial arrangements while respecting functional, aesthetic, and regulatory constraints?
        
        ### Methodology
        - Analyzed patterns in 200+ existing building designs
        - Developed generative models for suggesting spatial arrangements
        - Created constraint-based optimization algorithms for refining designs
        - Conducted user studies with practicing architects
        
        ### Key Contributions
        - Developed a novel representation of architectural spaces for machine learning
        - Created algorithms for optimizing spatial relationships based on usage patterns
        - Implemented interactive tools for architect-AI collaboration
        - Published findings in an architecture technology journal
        
        ### Results
        - Generated designs achieved 25% better space utilization
        - Architects reported 40% reduction in time spent on initial layout planning
        - Demonstrated successful integration of AI tools into existing design workflows
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies and Methods used:**")
        skills = ["Python", "TensorFlow", "Generative Models", "CAD Integration", "Constraint Programming", "User Interface Design", "Space Syntax Analysis", "Architecture Software"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Software Development Projects
with project_tabs[2]:
    # Directory section
    st.markdown('<div class="directory-card">', unsafe_allow_html=True)
    st.markdown("### Directory")
    st.markdown("Navigate to specific projects:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Project 1 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('smart-home').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Smart Home Automation System</div>
                <div class="directory-description">A comprehensive system integrating IoT devices for home automation and control.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 2 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('mobile-app').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Cross-Platform Mobile Application</div>
                <div class="directory-description">A Flutter-based mobile app for health monitoring and fitness tracking.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        # Project 3 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('web-platform').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Educational Web Platform</div>
                <div class="directory-description">An interactive web platform for online learning and educational content delivery.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 4 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('ar-app').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">AR Navigation Application</div>
                <div class="directory-description">An augmented reality app for indoor navigation and information overlay.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 1: Smart Home Automation
    st.markdown('<div id="smart-home" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Smart Home Automation System")
    st.markdown("**Duration:** March 2022 - December 2022")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/smart-home-concept-illustration_114360-1025.jpg", caption="Smart Home System")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed a comprehensive smart home automation system integrating various IoT devices and central control mechanisms as part of a university project team.
        
        ### Challenge
        Creating an integrated system that could connect multiple IoT devices from different manufacturers while providing a unified, intuitive control interface.
        
        ### Solution
        We developed a system featuring:
        - Central hub based on Raspberry Pi to coordinate different IoT protocols
        - Custom middleware to translate between different device communication standards
        - Mobile application providing intuitive controls and automation scheduling
        - Voice recognition integration for hands-free operation
        
        ### Key Contributions
        - Designed the system architecture for connecting multiple IoT devices
        - Implemented the central control hub using Raspberry Pi
        - Created a mobile application for remote control using Flutter
        - Integrated voice control capabilities through a custom API
        
        ### Results
        - Successfully connected and controlled 15+ devices from 5 different manufacturers
        - Reduced energy consumption in the test environment by 23% through smart automation
        - Received university innovation award for practical application
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Python", "IoT", "Raspberry Pi", "Flutter", "Mobile App Development", "API Integration", "Voice Recognition"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 2: Mobile App
    st.markdown('<div id="mobile-app" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Cross-Platform Mobile Application")
    st.markdown("**Duration:** July 2022 - October 2022")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/fitness-tracker-concept-illustration_114360-1525.jpg", caption="Mobile App")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed a cross-platform mobile application for health monitoring and fitness tracking with personalized recommendations.
        
        ### Challenge
        Creating a unified user experience across iOS and Android while integrating with various health tracking devices and providing personalized insights.
        
        ### Solution
        Implemented an application featuring:
        - Cross-platform framework with Flutter for consistent UI/UX
        - Bluetooth integration for various health tracking devices
        - Local data storage with encryption for sensitive health information
        - Machine learning-based recommendation engine for workout plans
        
        ### Key Contributions
        - Designed the application architecture and UI/UX
        - Implemented the Bluetooth communication protocols
        - Created the recommendation system using on-device ML
        - Developed the data visualization components
        
        ### Results
        - Achieved 10,000+ downloads in first three months
        - Maintained 4.7/5 average rating across app stores
        - Selected as featured health app on regional app stores
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Flutter", "Dart", "Firebase", "Bluetooth LE", "TensorFlow Lite", "SQLite", "UI/UX Design", "RESTful APIs"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 3: Educational Web Platform
    st.markdown('<div id="web-platform" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Educational Web Platform")
    st.markdown("**Duration:** January 2021 - May 2021")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/learning-concept-illustration_114360-6186.jpg", caption="Educational Platform")
    
    with col2:
        st.markdown("""
        ### Overview
        Designed and developed an interactive web platform for online learning focused on programming and data science education.
        
        ### Challenge
        Creating an engaging, interactive learning experience that could teach complex technical concepts while providing real-time feedback and progress tracking.
        
        ### Solution
        Built a platform with:
        - Interactive coding environments with real-time execution
        - Progressive learning modules with adaptive difficulty
        - Integrated assessment and feedback systems
        - Collaborative features for group learning
        
        ### Key Contributions
        - Architected the web application and database structure
        - Implemented the interactive code execution environment
        - Developed the learning path algorithms
        - Created visualization tools for complex concepts
        
        ### Results
        - Adopted by two university courses as a supplementary learning platform
        - 85% of students reported improved understanding of programming concepts
        - Over 500 active monthly users during the pilot phase
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["React", "Node.js", "MongoDB", "Docker", "WebSockets", "Authentication", "Code Sandbox", "D3.js"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 4: AR Navigation Application
    st.markdown('<div id="ar-app" class="project-card">', unsafe_allow_html=True)
    st.markdown("## AR Navigation Application")
    st.markdown("**Duration:** November 2021 - March 2022")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/augmented-reality-isometric-composition-with-people-using-ar-applications-smartphones-tablets-3d-vector-illustration_1284-84137.jpg", caption="AR Navigation App")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed an augmented reality mobile application for indoor navigation and information overlay within university buildings.
        
        ### Challenge
        Creating accurate indoor positioning and navigation without GPS, while overlaying contextual information in a user-friendly way.
        
        ### Solution
        Implemented an application with:
        - Computer vision-based positioning using architectural features
        - SLAM techniques for mapping and localization
        - QR code integration for initial positioning
        - Intuitive AR interface for directional guidance and information display
        
        ### Key Contributions
        - Designed the AR interface and navigation experience
        - Implemented the computer vision algorithms for positioning
        - Created the indoor mapping system
        - Developed the contextual information display system
        
        ### Results
        - Successfully deployed in three university buildings
        - Reduced average time for new visitors to find destinations by 70%
        - 92% user satisfaction rating in post-deployment surveys
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Unity3D", "ARCore", "ARKit", "Computer Vision", "SLAM", "C#", "Mobile Development", "UX Design"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Tab 4: Data Science Projects
with project_tabs[3]:
    # Directory section
    st.markdown('<div class="directory-card">', unsafe_allow_html=True)
    st.markdown("### Directory")
    st.markdown("Navigate to specific projects:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Project 1 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('data-viz').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Data Visualization Dashboard</div>
                <div class="directory-description">Interactive dashboard for analyzing urban mobility patterns using transportation data.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 2 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('nlp-project').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">NLP for Academic Research</div>
                <div class="directory-description">Natural language processing tools for analyzing academic papers and research trends.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        # Project 3 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('predictive-model').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Predictive Maintenance Model</div>
                <div class="directory-description">Machine learning model to predict equipment failures before they occur.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Project 4 directory item
        st.markdown(
            f"""
            <div class="directory-item" onclick="document.getElementById('image-analysis').scrollIntoView({{behavior: 'smooth'}})">
                <div class="directory-title">Architectural Image Analysis</div>
                <div class="directory-description">Computer vision system for analyzing architectural designs and identifying patterns.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 1: Data Visualization Dashboard
    st.markdown('<div id="data-viz" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Data Visualization Dashboard")
    st.markdown("**Duration:** September 2021 - January 2022")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/gradient-infographic-element-collection_23-2148413361.jpg", caption="Data Visualization")
    
    with col2:
        st.markdown("""
        ### Overview
        Created an interactive data visualization dashboard for analyzing urban mobility patterns in Beijing as part of a data science course project.
        
        ### Challenge
        Making complex transportation datasets accessible and meaningful to urban planners and policy makers who may not have data science backgrounds.
        
        ### Solution
        I developed an interactive dashboard that:
        - Processed and visualized large-scale public transportation and ride-sharing data
        - Created intuitive visualizations showing traffic patterns, peak usage times, and congestion hotspots
        - Implemented interactive filtering to explore data across different dimensions
        - Provided predictive insights about future mobility trends
        
        ### Key Contributions
        - Collected and cleaned large datasets of urban transportation data
        - Designed interactive visualizations for pattern recognition
        - Implemented the dashboard using Python web frameworks
        - Presented findings to urban planning departments
        
        ### Results
        - Dashboard was used by local transportation authority to analyze peak congestion patterns
        - Findings contributed to the adjustment of bus schedules in certain high-traffic areas
        - Project received highest grade in the data science course
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Python", "Streamlit", "Pandas", "Plotly", "Data Analysis", "GeoPandas", "Statistical Modeling"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 2: NLP Project
    st.markdown('<div id="nlp-project" class="project-card">', unsafe_allow_html=True)
    st.markdown("## NLP for Academic Research")
    st.markdown("**Duration:** February 2023 - August 2023")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/realistic-document-concept-illustration_23-2148921418.jpg", caption="NLP Research")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed natural language processing tools to analyze academic papers and identify research trends in robotics and HCI fields.
        
        ### Challenge
        Processing thousands of academic papers to extract meaningful insights about research trends, collaborations, and emerging topics.
        
        ### Solution
        Created a comprehensive NLP pipeline:
        - Automated scraping and parsing of academic papers from multiple sources
        - Applied text processing and topic modeling to identify research themes
        - Developed citation network analysis to map research influence
        - Created visualization tools for exploring the research landscape
        
        ### Key Contributions
        - Designed specialized NLP algorithms for technical academic content
        - Implemented topic modeling and trend analysis tools
        - Created network visualization for research collaborations
        - Developed a web interface for exploring the research database
        
        ### Results
        - Analyzed over 15,000 academic papers from major robotics and HCI conferences
        - Identified 5 emerging research trends before they became widely recognized
        - Tool was adopted by two research labs for literature review assistance
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies and Methods used:**")
        skills = ["Python", "NLTK", "spaCy", "Transformers", "Topic Modeling", "Network Analysis", "Web Scraping", "Django"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 3: Predictive Maintenance
    st.markdown('<div id="predictive-model" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Predictive Maintenance Model")
    st.markdown("**Duration:** March 2022 - July 2022")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/factory-worker-operating-industrial-mill-machine_74855-11058.jpg", caption="Predictive Maintenance")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed a machine learning model to predict equipment failures before they occur, enabling proactive maintenance scheduling.
        
        ### Challenge
        Creating a robust prediction model that could work with limited historical failure data while minimizing both false positives and false negatives.
        
        ### Solution
        Implemented an end-to-end predictive maintenance system:
        - Sensor data collection and preprocessing pipeline
        - Feature engineering to extract meaningful patterns from time-series data
        - Ensemble machine learning model combining multiple prediction approaches
        - Alert system with customizable sensitivity levels
        
        ### Key Contributions
        - Designed the data collection and preprocessing framework
        - Developed novel feature extraction methods for mechanical systems
        - Created and optimized the machine learning models
        - Implemented the alert and visualization system
        
        ### Results
        - Reduced unexpected equipment downtime by 65%
        - Decreased maintenance costs by 30% through optimized scheduling
        - Achieved 89% prediction accuracy with 2-week advance notice
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Python", "Scikit-learn", "Time Series Analysis", "Feature Engineering", "Ensemble Methods", "IoT Sensors", "Signal Processing", "Database Design"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 4: Architectural Image Analysis
    st.markdown('<div id="image-analysis" class="project-card">', unsafe_allow_html=True)
    st.markdown("## Architectural Image Analysis")
    st.markdown("**Duration:** April 2020 - December 2020")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img.freepik.com/free-vector/blueprint-background-design_23-2148594539.jpg", caption="Architectural Analysis")
    
    with col2:
        st.markdown("""
        ### Overview
        Developed a computer vision system for analyzing architectural designs and automatically identifying stylistic patterns and spatial arrangements.
        
        ### Challenge
        Creating algorithms that could effectively identify architectural features and styles across diverse building designs and blueprint formats.
        
        ### Solution
        Built a comprehensive image analysis system:
        - Preprocessing pipeline for various architectural document formats
        - Feature extraction for identifying key architectural elements
        - Classification models for architectural styles and periods
        - Spatial analysis tools for room layout and circulation patterns
        
        ### Key Contributions
        - Developed specialized computer vision algorithms for architectural drawings
        - Created a database of tagged architectural features
        - Implemented style classification using transfer learning
        - Designed spatial analysis tools for building layouts
        
        ### Results
        - Successfully identified architectural styles with 85% accuracy
        - Automated the analysis of 500+ building designs for a research project
        - Tools integrated into an architecture department's educational resources
        """)
        
        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        st.markdown("**Technologies used:**")
        skills = ["Python", "OpenCV", "TensorFlow", "Image Processing", "Transfer Learning", "CAD Integration", "Spatial Analysis", "Database Management"]
        
        # 将技能分成多列显示
        cols = st.columns(4)  # 创建4列
        for i, skill in enumerate(skills):
            with cols[i % 4]:  # 循环使用这4列
                st.markdown(f"<div style='background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-bottom: 8px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Additional info
st.markdown('<h2 class="section-header">More Projects</h2>', unsafe_allow_html=True)
st.write("These are just a few highlights of my work. I'm always working on new projects and exploring new technologies.")
st.write("If you'd like to discuss any of these projects in more detail or explore potential collaborations, please feel free to contact me through the Contact page.")

# GitHub link
st.markdown("### Check out my code")
st.markdown("You can explore more of my projects and code samples on my [GitHub profile](https://github.com).")

# Add JavaScript for smooth scrolling
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Fix for clicking on directory items
    document.querySelectorAll('.directory-item').forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('onclick').match(/document.getElementById\\('(.*?)'\\)/)[1];
            document.getElementById(targetId).scrollIntoView({behavior: 'smooth'});
        });
    });
});
</script>
""", unsafe_allow_html=True)