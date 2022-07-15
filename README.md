# <span style='font-family:georgia'>"Robot Reviews: Let the AI Choose": a Project by Blurred\-Futures</span>

<span style='font-family:georgia'>Welcome, here at Blurred\-Futures, we created an AI system that can generate positive or negative reviews of a video game provided by the user, even if it doesn't exist! It has additional features such as adjustable review length, temperature \(how creative the AI should be\), and the amount of reviews. </span>

<span style='font-family:georgia'>If you have any questions, feel free to open an issue on </span>[<span style='font-family:georgia'>Github</span>](https://github.com/organization-x/omni/issues)<span style='font-family:georgia'>.</span>

### <span style='font-family:georgia'>Background</span>

<span style='font-family:georgia'>We went with this project idea because it related to something everyone in our group had an interest in, which we thought would make the project more enjoyable. It also serves a practical use. When compared to the greater consumer pool of video games, people who write reviews are surprisingly few. The game industry could be improved by review sharing becoming more convenient to the public, thus allowing more reasonable feedback from people beyond those who love, hate, or are intrigued enough about the game to draft a review.</span>

<span style='font-family:georgia'>This guide covers how you can quickly deploy most projects with the </span>[<span style='font-family:georgia'>Flask</span>](https://flask.palletsprojects.com/)<span style='font-family:georgia'> framework and our omni scaffold.</span>

### <span style='font-family:georgia'>Datasets</span>

<span style='font-family:georgia'>We ended up using 2 different datasets from Kaggle. They included: game name, review text, about 6.2 million publicly known reviews we acquired, and of course, this includes negative and positive reviews. In addition, we used a dataset of game sales in order to add genre specification.  </span>

### <span style='font-family:georgia'>Model</span>

For this project, we trained a GPT\-Neo model, even though it's slow, it can produce the best results. GPT Neo was chosen over alternatives like GPT-2 for this reason. It is a Transformer (A type of deep learning) model with over 2 billion parameters. We trained multiple times and it was long and tedious work, training would take up to 5 hours at some points. 

## <span style='font-family:georgia'>Challenges</span>

<span style='font-family:georgia'>This project was never easy at any point. Before using the data for training, we had to make sure it was accurate and cleaned out beforehand. Deleting specific words, HTML's, emails, and fine\-tuning would take time and patience. Another somewhat small problem was the lack of RAM at some point, making the system crash and stop working entirely. </span>

<span style='font-family:georgia'>If you want to recreate this project, please be sure to train the model and thoroughly preprocessed data. It helps to use the .sample\(\) function to shorten our key dataset, which has over 6 million indexes. Values in the hundreds of thousands should do pretty well. Also, you'll want to save the data / model as changes happen frequently in case anything happens.</span>

### <span style='font-family:georgia'>Recourses Needed</span>

<span style='font-family:georgia'>The files/directories which you will need to edit are </span><span style='font-family:georgia'>**bolded**</span><span style='font-family:georgia'>, and the files you </span><span style='font-family:georgia'>**may**</span><span style='font-family:georgia'> need to edit are </span><span style='font-family:georgia'>_italicized_</span><span style='font-family:georgia'>.</span>

- <span style='font-family:georgia'>Kaggle Dataset: </span>[<span style='font-family:georgia'>https://www.kaggle.com/datasets/andrewmvd/steam\-reviews6</span>](https://www.kaggle.com/datasets/andrewmvd/steam-reviews)
- Google Colab Notebook: https://colab.research.google.com/drive/1L9Zfc50kTDwnfQQBauduAeteHq7qGC-X#scrollTo=i5uWbdFGBQql
- Python (Flask)
- aitextgen
- HTML
- CSS
- Any cell that includes the term "gdown" is for copying a path, which will require you to go to the file folder on the left, open the respective folder that the data or model is in, copy the path, and paste there.
- Otherwise, feel free to simply follow the cells in order.
- Note: When you get to model training, which ideally takes about 3 hours, please consistently monitor the Colab tab. Inactivity for too long will stop the runtime and slow training down.


## <span style='font-family:georgia'>Links for Models</span>

You also need to download both models we trained: one outputs positive reviews, the other outputs negative ones.

Negative: https://drive.google.com/drive/folders/1yikfCo0KmmYsLfybCsMAeVxO0rYcoXpH?usp=sharing

Positive : https://drive.google.com/drive/folders/1pj5qoWX_R0qRDqV4OIZqtmgUfUIiafIT?usp=sharing


Screenshots

![Home Page](https://github.com/ghoshdebapratim1/game-review-bot/blob/bb896430f27e4568d642a602a5b72c2730bc6b84/app/static/img/Screenshot%202022-07-14%202.14.56%20PM.png)

![Model Page](https://github.com/ghoshdebapratim1/game-review-bot/blob/bb896430f27e4568d642a602a5b72c2730bc6b84/app/static/img/Screenshot%202022-07-14%202.15.16%20PM.png)

### <span style='font-family:georgia'>The Team</span>

<span style='font-family:georgia'>Pierce Lilly - Project Manager and Data Scientist </span>

<span style='font-family:georgia'>Nicholas Dai - Frontend Engineer</span>

<span style='font-family:georgia'>Ailesh Sadruddin - Machine Learning Engineer</span>

<span style='font-family:georgia'>Roonal Salcedo - Machine Learning Engineer</span>

<span style='font-family:georgia'>Keegan Hosch - Frontend Engineer</span>

<span style='font-family:georgia'>Nathan Nipp  \- Backend Engineer</span>

<span style='font-family:georgia'>Deb Ghosh \- Mentor</span>

<span style='font-family:georgia'>We all worked hard 
  to accomplish our goal, for hours we put in our all to reach our desired end goal. Everyone on the team was more than pleased with the final outcome.</span>

