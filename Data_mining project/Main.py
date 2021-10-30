import Read_Data
import Pre_Processing
import SVM_Classification
from sklearn.model_selection import train_test_split

if __name__ == '__main__':

    # reads and processes the csv file
    csv_dataframe = Read_Data.read_csv(file_name='rt-polaritydata/rt-polarity.pos')
    reports1,labels1=Read_Data.process_data(data=csv_dataframe,type='pos')

    csv_dataframe1=Read_Data.read_csv(file_name='rt-polaritydata/rt-polarity.neg')
    reports2, labels2 = Read_Data.process_data(data=csv_dataframe1,type='neg')

    reports=reports1+reports2

    print(len(reports))

    labels=labels1+labels2

    unique_list = sorted(list(set(labels)))

    for item in unique_list:
        print('{} = {}'.format(item, labels.count(item)))

    # tokenize and pre-process reports
    tokenized_reports = Pre_Processing.tokenize_preprocess_corpus(reports)

    print(tokenized_reports[3])

    # # Divide the reports and labels into Training  and Test Documents

    train_reports,test_reports,train_labels,test_labels  = train_test_split(tokenized_reports, labels, test_size = 0.33, random_state=42)

    # Do the classification!!
    SVM_Classification.SVM_Normal(trainDoc=train_reports, trainClass=train_labels,
                                  testDoc=test_reports, testClass=test_labels, tfIdf=True)





