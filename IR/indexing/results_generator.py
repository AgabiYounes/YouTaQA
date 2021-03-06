import getopt
import json
import os.path
import sys
from tqdm import tqdm
import lucene
from org.apache.lucene.search.similarities import *
from search import Searcher


class ResultsGenerator:

    def __init__(self, index_dir):
        self.searcher = Searcher(index_dir)

    def get_id_section(self, request):
        idList = list()
        for i in range(len(request)):
            hitDoc = self.searcher.searcher.doc(request[i].doc)
            idList.append(hitDoc.get("id_section"))
        return idList

    def process(self, input_file, index_dir, output_dir):
        output_file_1 = open(
            output_dir + "/results_BM25_1.txt", 'a+', encoding="utf-8")
        output_file_2 = open(
            output_dir + "/results_BM25_2.txt", 'a+', encoding="utf-8")
        output_file_3 = open(
            output_dir + "/results_BM25_3.txt", 'a+', encoding="utf-8")
        output_file_4 = open(
            output_dir + "/results_BM25_4.txt", 'a+', encoding="utf-8")
        output_file_5 = open(
            output_dir + "/results_VSM_1.txt", 'a+', encoding="utf-8")
        output_file_6 = open(
            output_dir + "/results_VSM_2.txt", 'a+', encoding="utf-8")
        output_file_7 = open(
            output_dir + "/results_VSM_3.txt", 'a+', encoding="utf-8")
        output_file_8 = open(
            output_dir + "/results_VSM_4.txt", 'a+', encoding="utf-8")

        num_lines = 0
        with open(input_file, encoding="utf-8") as json_file:
            data = json.load(json_file)
            for p in data['data']:
                for par in p['paragraphs']:
                    for q in par["qas"]:
                        num_lines += 1

        with tqdm(total=num_lines) as pbar:
            with open(input_file, encoding="utf-8") as json_file:
                data = json.load(json_file)
                for p in data['data']:
                    title = p["title"]
                    for par in p['paragraphs']:
                        for q in par["qas"]:
                            pbar.update(1)
                            if q["is_impossible"] is False:
                                question_content_s_BM25 = self.searcher.simpleSearch(
                                    q["question"], BM25Similarity())
                                id_question_content_s_BM25 = self.get_id_section(question_content_s_BM25)
                                    
                                question_title_content_s_BM25 = self.searcher.pairSearch(
                                    [title, q["question"]], BM25Similarity())
                                id_question_title_content_s_BM25 = self.get_id_section(question_title_content_s_BM25)
                                
                                question_content_m_BM25 = self.searcher.multiFieldsSearch(
                                    q["question"], BM25Similarity())
                                id_question_content_m_BM25 = self.get_id_section(question_content_m_BM25)
                                
                                question_title_content_m_BM25 = self.searcher.multiFieldsPairSearch(
                                    [title, q["question"]], BM25Similarity())
                                id_question_title_content_m_BM25 = self.get_id_section(question_title_content_m_BM25)

                                question_content_s_TDF = self.searcher.simpleSearch(
                                    q["question"], ClassicSimilarity())
                                id_question_content_s_TDF = self.get_id_section(question_content_s_TDF)
                                
                                question_title_content_s_TDF = self.searcher.pairSearch(
                                    [title, q["question"]], ClassicSimilarity())
                                id_question_title_content_s_TDF = self.get_id_section(question_title_content_s_TDF)
                                
                                question_content_m_TDF = self.searcher.multiFieldsSearch(
                                    q["question"], ClassicSimilarity())
                                id_question_content_m_TDF = self.get_id_section(question_content_m_TDF)
                                
                                question_title_content_m_TDF = self.searcher.multiFieldsPairSearch(
                                    [title, q["question"]], ClassicSimilarity())
                                id_question_title_content_m_TDF = self.get_id_section(question_title_content_m_TDF)

                                for i in range(len(question_content_s_BM25)):
                                    output_file_1.write(
                                        q["id"] + " Q0 " + str(id_question_content_s_BM25[i]) + " " + str(i+1) + " " + str(question_content_s_BM25[i].score) + " STANDARD\n")
                                for i in range(len(question_title_content_s_BM25)):
                                    output_file_2.write(
                                        q["id"] + " Q0 " + str(id_question_title_content_s_BM25[i]) + " " + str(i+1) + " " + str(question_title_content_s_BM25[i].score) + " STANDARD\n")
                                for i in range(len(question_content_m_BM25)):
                                    output_file_3.write(
                                        q["id"] + " Q0 " + str(id_question_content_m_BM25[i]) + " " + str(i+1) + " " + str(question_content_m_BM25[i].score) + " STANDARD\n")
                                for i in range(len(question_title_content_m_BM25)):
                                    output_file_4.write(
                                        q["id"] + " Q0 " + str(id_question_title_content_m_BM25[i]) + " " + str(i+1) + " " + str(question_title_content_m_BM25[i].score) + " STANDARD\n")
                                for i in range(len(question_content_s_TDF)):
                                    output_file_5.write(
                                        q["id"] + " Q0 " + str(id_question_content_s_TDF[i]) + " " + str(i+1) + " " + str(question_content_s_TDF[i].score) + " STANDARD\n")
                                for i in range(len(question_title_content_s_TDF)):
                                    output_file_6.write(
                                        q["id"] + " Q0 " + str(id_question_title_content_s_TDF[i]) + " " + str(i+1) + " " + str(question_title_content_s_TDF[i].score) + " STANDARD\n")
                                for i in range(len(question_content_m_TDF)):
                                    output_file_7.write(
                                        q["id"] + " Q0 " + str(id_question_content_m_TDF[i]) + " " + str(i+1) + " " + str(question_content_m_TDF[i].score) + " STANDARD\n")
                                for i in range(len(question_title_content_m_TDF)):
                                    output_file_8.write(
                                        q["id"] + " Q0 " + str(id_question_title_content_m_TDF[i]) + " " + str(i+1) + " " + str(question_title_content_m_TDF[i].score) + " STANDARD\n")
                                
        print("==> Results successfully created.\n")

def main(argv):
    """
    Main function that read input arguments to lunch the script.
    :param argv:
    :return:
    """

    input_file = ''
    output_dir = ''
    index_dir = ''
    try:
        opts, args = getopt.getopt(
            argv, "hi:d:o:", ["ifile=", "dfile=", "ofile="])
    except getopt.GetoptError:
        print('results_generator.py -i <input_file> -d <index_dir> -o <output_folder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
                'results_generator.py -i <input_file> -d <index_dir> -o <output_folder>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
            if not os.path.isfile(input_file):
                print(input_file + ' does not exist.')
                print("\n")
                sys.exit(2)
        elif opt in ("-o", "--ofile"):
            output_dir = arg
            if not os.path.isdir(output_dir):
                print(output_dir + ' does not exist.')
                print("\n")
                sys.exit(2)
        elif opt in ("-d"):
            index_dir = arg
            if not os.path.isdir(index_dir):
                print(index_dir + ' does not exist.')
                print("\n")
                sys.exit(2)

    if input_file != '' and output_dir != '' and index_dir != '':
        rg = ResultsGenerator(index_dir)
        rg.process(input_file, index_dir, output_dir)
    else:
        print('results_generator.py -i <input_file> -d <index_dir> -o <output_folder>')
        sys.exit(2)


if __name__ == "__main__":
    """
    The main function.
    """
    main(sys.argv[1:])
