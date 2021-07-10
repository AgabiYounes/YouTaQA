# YouTaQA 
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/AgabiYounes/YouTaQA)
YouTaQA is a powerful Q&A system that provides a complete pipeline. Unlike existing QA systems, our system allows users to have accurate answers to their questions based entirely on our search engine, saving the user from having to provide anything other than the question, and possibly making their task easier.
To achieve the objective of our system, as shown in the general diagram, we've conceived an architecture composed of three basic modules and an UI where the users enter their questions:

-   A search engine (MRI) that serves to provide the 5 most relevant contexts to a given question.
-   A module of context classiﬁcation (MC) based on BERT to choose and identify among the 5 search engine results the best context likely to contain the correct answer to the question.
-   Answer Extraction module (MER) based on BERT that extracts the correct answer from the context chosen by classiﬁier in the previous step.
    ![YouTaQA Structure](/Paper/Figures/schemaGlobal.png)

## Installation

In order to use our system, you will need to install the following packages using pip:

-   tqdm 4.47.0
-   pathlib
-   sklearn
-   nltk.corpus
-   numpy 1.19.0
-   tokenizers 0.8.1rc1
-   jupyter
-   xml.dom
-   torch  1.5.1
-   torchvision 0.6.1
-   transformers
-   django
-   matplotlib  3.2.2

In addition, you need to install nltk stop words by launching the linux/MacOS terminal (this project has been tested on version 3.8.0) and apply the following steps:

> python
>
> import nltk
>
> nltk.download(stopwords)

For the search engine, you need to install PyLucene by [following this tutorial](https://medium.com/@michaelaalcorn/how-to-use-pylucene-e2e2f540024c).

**PS**: In order to install PyLucene properly, after downloading pylucene, you must put the `/IR/indexing/PythonEnglishAnalyzer.java` file in the `pylucene-8.3.0/java/org/apache/pylucene/analysis` folder before starting the installation.

## Wikipedia preprocessing

Before starting wikipedia indexing, we split each wikipedia article into its own file, in a well-structured tree structure (For more information, please see the project [paper](/Paper)).

To do this, you have to download the dump from [wikipedia](https://tools.wmflabs.org/thibtools/dump-torrents/enwiki-20200401-pages-articles-multistream.xml.bz2.torrent) and decompress it. Then run the `IR/preprocessing/parse.py` script with the command: 

> parse.py -i &lt;input_file> -o &lt;output_file>

where `input_file` is the folder of the previously uncompressed wikipedia dump and `output_file` is the output folder where to put the article files (you need to allow 200GB space on the disk).

## Document indexing

To index documents, you need to run the IR/indexing/indexer.py script with the command :

> index.py -i &lt;input_folder> -o &lt;output_folder>

Where `input_folder` is the folder that contains the result of the preprocessing (the folder that contains the files of the Wikipedia articles) and `output_folder` is the directory in which the index will be saved.

## Context classification module

### Training of the model

Our classification model is based on [BERT](https://github.com/google-research/bert) and [transformers](https://github.com/huggingface/transformers), it allows a score of **F1=80%**. In order to train the classification model, you just have to download the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/) and put the `train set` and the `dev set` files in the `/DeepLearning/Classifier/Data` folder and run the script `/DeepLearning/Classifier/training_classifier.py`.

## Answer Extraction module

### Training of the model

To train the answer extraction model, please follow the steps indicated on the transformers [project](https://github.com/huggingface/transformers/tree/master/examples/question-answering). This model scores an **F1_score=92%** and an **Exact_match=87**.

## Launching the YouTaQA application

![YouTaQA Logo](/Paper/Figures/exempleSystemeYouTaQA.png)

After finishing the previous steps, it is time to run and launch the web application of our YouTaQA system. To do this, you must first change the paths in `/Web application/myproject/setting.py` following the paths of your configuration (index path, classification model path, etc). After that, you can start the django server by running the script `/Web application/manage.py` with the following command : 

> Python manage.py runserver

Then, open the browser in the port indicated in the terminal.

For more information, you can read the PDF [paper](/Paper) of this project or contact one of the developers responsible for this project:

-   [Rayane Younes AGABI](https://github.com/AgabiYounes)
-   [Mohamed Reda Bouadjenek](https://github.com/rbouadjenek)
-   [Asma Tidafi](https://github.com/AsLibDev)
