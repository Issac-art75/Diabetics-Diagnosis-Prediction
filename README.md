# TITLE : Diabetes Diagnosis Prediction System

# ABSTRACT: 
Diabetes mellitus, commonly known as diabetes is a chronic disease which affects a majority of people globally. Diabetes causes due to Age, lack of exercise, Obesity, bad diet, high blood pressure etc.., According to International Diabetes Federation 382 million people are living with diabetes across the whole world. Diabetics causes Blindness, kidney failure, heart attacks and Strokes. By 2035, this will be doubled as 592 million patients. Diabetics can only be kept only under control and cannot be cured. Our main goal is to unlock the power of technology to help people finding whether they are being affected by this disease. Diagnosis prediction system for Diabetes are already present in the medical industry. But they failed to diagnose accurately. The Proposed system is based on Logistic Regression, a machine learning model. The Dataset is taken from Kaggle.com website and is originally developed by PIMA which contains 768 data with the following features: Pregnancy, Glucose, BP, Skin-thickness, insulin, BMI, Diabetes Pedigree function, Age. Since we have so many features  to train the system with, it makes the system more reliable and trustable. Exploring important features of diabetes makes it possible for the diagnosis system to accurately predict whether the person is being  affected or not. Experiment results shows that it produces an accuracy of 96%.  

# INTODUCTION: 
Diabetes mellitus by the definition of the WHO, is a disease caused by insufficient insulin production in the pancreas. Having this disease is a serious issue. At early stages, it is unnoticeable As it doesn’t give any symptoms. But when detected late, it can cause serious health complications such as heart attack, blindness and kidney failure and even premature death. Life Expectancy will shorten by 5 to 10 years. An early diagnosis of this disease can significantly increase the life expectancy of the patient [2]. 

Diabetes is caused by 2 reasons. One is the inability of the body to produce enough insulin. Other one is cells couldn’t respond to the insulin that is produced in the body. There are 3 types of diabetes. Type 1 Diabetes, Type 2 Diabetes and gestational diabetes. Among these types, Type 2 Diabetes is the most prevalent one. Developing countries are the one’s which are highly affected by diabetes. According to WHO, in 1980, 100+ million people were affected by diabetes whereas in 2014, 400+ million people were affected by this disease. And the situation is dangerously and exponentially getting increased. This disease also has an economic impact. For Example, in United States alone, it costs upto 132 billion dollars every year. All types of Diabetes are dangerous and lead to complications which can further increase the chance of premature death. Statistics also tells us that the people affected by diabetes has 50% chance on getting heart disease and stroke and it may increase in the near future [3] .

Moreover, the traditional method requires the doctor to conduct multiple tests on the patients. Based on the test results, Doctors evaluate whether the patent is being affected by the diabetes or not. By Exploiting the advancement and improvement of technology in recent days, we are introducing a system which will play the role of a doctor. The System uses Logistic Regression model to recognize the pattern and find the result. The system is fed with a dataset which is originally developed by PIMA. This System is moreover used by the lab technician rather than the patient itself. Lab Technician should enter the inputs and click on submit on the Website. Then the system evaluates and shows the results in 2 categories – Positive and Negative. 

# LITERATURE REVIEW:
[1]   Mingqi  Li,   Xiaoyang  Fu and   Dongdong  Li     (2019)
proposed a system in which they implemented XGBoost Algorithm. They used the PIMA dataset, which is commonly used. They also compared with 6 different Machine algorithms and found out that XGBoost and LR algorithms are doing best.

[2] Amelec Viloriaa, Yaneth Herazo-Beltranb, Danelys Cabrerac, Omar Bonerge Pinedad (2020) concluded that blood test is not enough to identify the disease. They used Support Vector Machine (SVM) algorithm. BMI, blood glucose concentration and prior medical diagnosis of DM of 500 patients from a public hospital in Colombia has been taken as the dataset.

[3] Swapna G, Soman KP, and VinayaKumar R (2018) proposed a system which evaluates by the analysis of Heart Rate Variability (HRV) signals obtained from ECG Signals. 
The ECG of 20 diabetes patients and 20 normal people were collected. The people were asked to be in a supine position for 10 minutes. They implemented CNN algorithm and obtained an accuracy of 93.6%.  

[4] A.Mujumdar, V. Vaidehi (2019) proposed a system implementing K-means Clustering algorithm. They also used the most commonly used PIMA dataset. They also compared the results with many other algorithms like DecisionTree, Random Forest, KNN etc… They concluded that Logistic Regression gave the highest accuracy of 96%.

[5] Chollette C. Olisah , Lyndon Smith and Melvyn Smith (2022) proposed a system which implements 2GDNN algorithm. They used 2 datasets namely PIMA and LMCH. In this paper, 6 algorithms are compared. They concluded that 2GDNN was the best performing one with an accuracy of 96.67%.

[6] Leon Kopitar, Primoz Kocbek, Leona Cilar, Aziz Sheikh, & Gregor Stiglic (2020) proposed a paper in which they compare different algorithms with 5 different datasets. They concluded that linear regression model performed with the lowest root mean square error and XGBoost with the highest root mean square error.

[7] Nazin Ahmeda, Rayhan Ahammeda, Md. Manowarul Islama, Md. Ashraf Uddina, Arnisha Akhter, Md. Alamin Talukder, Bikash Kumar Paul (2021) proposed a system where they have implemented a web application using flask framework. They compared the performance with different ML models and selected the best among those. They concluded that SVM outperforms other algorithms and adopted it.

[8] Umair Muneer Butt, Sukumar Letchmunan, Mubashir Ali, Fadratul Hafinaz Hassan, Anees Baqir,  and Hafiz Husnain Raza Sherazi (2021) performed analysis of 3 models namely: Logistic Regression, Random Forest, Multilayer perceptron. After doing performance analysis, they concluded that MLP outperformed other 2 algorithms with an accuracy of 86%. They fine-tuned the MLP algorithm before implementing in the system.

[9] KM Jyoti Rani (2020) implemented SVM algorithm. Initially they compared 5 different algorithms with PIMA dataset. Later, they concluded that Decision Tree performed well with the given dataset and achieved an accuracy of 99%.

[10] Tawfik Beghriche, Mohamed Djerioui, Youcef Brik, Bilal Attallah and Samir Brahim Belhaouari (2021) implemented a deep neural network algorithm. Initially they started to compare multiple algorithms including LR, SVM etc… They have used enhanced version of PIMA dataset which contains 2000 data containing 9 features

# OUTPUT: 
(a) Home page:  
![Output1](https://github.com/Issac-art75/Diabetics-Diagnosis-Prediction/assets/74670759/430a4f7a-f994-49cd-bc05-299200182f49) 
(b) Predict Page:  
![Output2](https://github.com/Issac-art75/Diabetics-Diagnosis-Prediction/assets/74670759/6c0c9abb-ba8f-4f47-b861-a3678beb4445) 
(c) Positive:  
![Output3](https://github.com/Issac-art75/Diabetics-Diagnosis-Prediction/assets/74670759/8362db64-3e06-4abd-903e-4ce3b465f534) 
![Output4](https://github.com/Issac-art75/Diabetics-Diagnosis-Prediction/assets/74670759/e198275b-08a4-46e5-a7df-4afc3f42a96b) 
(d) Negative:  
![Output5](https://github.com/Issac-art75/Diabetics-Diagnosis-Prediction/assets/74670759/d8ae3905-a8ed-4994-ad05-d0f5f11c00bf) 
![Output6](https://github.com/Issac-art75/Diabetics-Diagnosis-Prediction/assets/74670759/c995616c-46dd-49ff-b938-f7b7fdc7b409)

# RESULT:
       Thus a Machine Learning algorithm for Diabetes Diagnosis Prediction system has been implemented and executed successfully.






