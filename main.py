import openai

# Function to call OpenAI API with the provided resume content
def parse_resume_to_json(resume_content):
    prompt = f"""
    You are a JSON parser. I will provide you with the text content of a resume, and you need to extract and organize the information into a structured JSON format. The JSON should include the following fields:
    - Name
    - Contact Information
      - Email
      - Phone
      - Address
      - LinkedIn
      - GitHub
    - Projects
      - Title
      - Description
      - Technologies Used
      - Duration
    - Certificates
      - Title
      - Date
    - Achievements
    - Technical Skills
      - Languages
      - Technologies/Frameworks
      - Skills
    - Education
      - Degree
      - Institution
      - Location
      - CGPA
      - Duration

    Here is the resume content:

    {resume_content}

    Please provide the JSON output.
    """
    
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.3
    )

    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    resume_content = """
    Talari Nandeesh
    Rayachoti, Andhra Pradesh 516269
    8374990106
    nandeeshtalari33@gmail.com
    linkedin.com/in/nandeesh-talari/
    github.com/Nandeesh132/

    Projects
    - USA Adidas Sales Analysis Using Tableau | Tableau and R | Aug’23-Nov’23
      Created data analysis and visualization graphs and represented a dashboard for respective graphs drawn from 2020 to 2021 data of Adidas Sales in the USA. This project talks about in which zone more sales have been registered, which product produced more profit for retailers, which retailers have got more sales and profits, and in which month and dates respectively more sales and profit occurred.
    - Classification Machine Learning Algorithms on Student Stress Dataset | Rapid Miner and R | Aug’23-Oct’23
      Created a classification model on the Student Stress Level Dataset. This project helps to identify how the students are getting stressed and which stage it is.
    - Dashboard on Cases Registered in Police Stations in India | Tableau Prep and Excel | Aug’22-Oct’22
      Created some graphs using the dataset. This project talks about which states have a greater number of robbery cases registered, which states have more percentage of robbed items, and which states have recovered cases so far.
    - Scientific Calculator Project | GUI Tools and Python Programming | Sep’22-Dec’22
      It is a scientific calculator application. It is used to calculate the math functions easily. In this application, a scientific calculator helped to learn how to use GUI tools.

    Certificates
    - R | Mar 2023 | Introduction to R - Datacamp
    - Data Structures And Algorithms | Jun 2022 | Complete Interview Preparation- Self-Paced (DSA) by GFG
    - Tableau | Mar 2021 | Data Visualization-Tableau by LPU

    Achievements
    - Published research paper in the IEEE IATMSI 2024 conference based on the research project “Classification and Evaluation of Indian Faces Using Machine Learning Models” 2024.
    - Research paper accepted in the INCRITO 2024 conference based on the research project “Addressing Food Waste: Survey of Approaches Technological Innovations and Sustainable Solutions” 2024.

    Technical Skills
    - Languages: Java, R, Python
    - Technologies/Frameworks: Tableau, Excel, RapidMiner
    - Skills: Data Structures and Algorithms, Encryption and Decryption, Leadership, Problem-solving, Attentive, Sportive

    Education
    - Lovely Professional University, Punjab, India | Integrated B. Tech - M. Tech - Computer Science and Engineering | CGPA: 7.90 | Since August 2020
    - Narayana Junior College, Vijayawada, Andhra Pradesh | Intermediate | CGPA: 9.34 | April 2018 - March 2020
    - Narayana School, Vijayawada, Andhra Pradesh | Matriculation | CGPA: 9.70 | April 2017 - March 2018
    """
    
    json_output = parse_resume_to_json(resume_content)
    print(json_output)
