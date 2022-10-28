import matplotlib.pyplot as plt

def plot_curves(history, new_history = None, fine_tuning = False, initial_epochs = None):

  loss = history.history['loss']
  val_loss = history.history['val_loss']
  accuracy = history.history['accuracy']
  val_accuracy = history.history['val_accuracy']
 
  if fine_tuning:
    loss = history.history['loss'] + new_history.history['loss']
    val_loss = history.history['val_loss'] + new_history.history['val_loss']
    accuracy = history.history['accuracy'] + new_history.history['accuracy']
    val_accuracy = history.history['val_accuracy'] + new_history.history['val_accuracy']

  epochs = range(len(loss))

  plt. figure(figsize = (20,7))

  # Plot loss
  plt.subplot(1,2,1)
  plt.plot(epochs, loss, label = 'Training', c = 'b')
  plt.plot(epochs, val_loss, label = 'Validation', c = 'r')
  plt.title('Loss')
  plt.xlabel('Epochs')
  if fine_tuning:
    plt.plot([initial_epochs, initial_epochs],
              plt.ylim(), label='Fine Tuning', c = 'g')
  plt.legend();


  # Plot accuracy
  plt.subplot(1,2,2)
  plt.plot(epochs, accuracy, label = 'Training', c = 'b')
  plt.plot(epochs, val_accuracy, label = 'Validation', c = 'r')
  plt.title('Accuracy')
  plt.xlabel('Epochs')
  if fine_tuning:
    plt.plot([initial_epochs, initial_epochs],
              plt.ylim(), label='Fine Tuning', c = 'g')
  plt.legend();
