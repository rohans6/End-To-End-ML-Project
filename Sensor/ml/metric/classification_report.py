import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.metrics as metrics
def get_classification_report(y_train,y_train_pred,y_test,y_test_pred):
    train_f1_score=metrics.f1_score(y_train,y_train_pred)
    train_accuracy=metrics.accuracy_score(y_train,y_train_pred)
    train_precision=metrics.precision_score(y_train,y_train_pred)
    train_recall=metrics.recall_score(y_train,y_train_pred)

    test_f1_score=metrics.f1_score(y_test,y_test_pred)
    test_accuracy=metrics.accuracy_score(y_test,y_test_pred)
    test_precision=metrics.precision_score(y_test,y_test_pred)
    test_recall=metrics.recall_score(y_test,y_test_pred)
    print("Classification Report:-")
    print(f" Training F1 Score: {train_f1_score}")
    print(f"Testing F1 Score: {test_f1_score}")

    print(f"Training Accuracy: {train_accuracy}")
    print(f"Testing Accuracy: {test_accuracy}")

    print(f"Training Precision: {train_precision}")
    print(f"Testing Precision: {test_precision}")

    print(f"Training Recall: {train_recall}")
    print(f"Testing Recall: {test_recall}")

    return {'train_accuracy': train_accuracy,'test_accuracy': test_accuracy,'train_precision':train_precision,'test_precision': test_precision,'train_recall':train_recall,'test_recall': test_recall,'train_f1_score':train_f1_score,'test_f1_score': test_f1_score}
