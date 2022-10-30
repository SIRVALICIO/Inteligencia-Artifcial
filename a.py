def accuracy_metric(actual, predicted):
 correct = 0
 contador= 0
 for x in actual:
     if x == predicted[contador]:
         correct+=1
     contador+=1