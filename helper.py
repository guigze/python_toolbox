import matplotlib.pyplot as plt

def plot_curves(history):

  loss = history.history['loss']
  val_loss = history.history['val_loss']
  accuracy = history.history['accuracy']
  val_accuracy = history.history['val_accuracy']

  epochs = range(len(history.history['loss']))

  plt. figure(figsize = (20,7))

  # Plot loss
  plt.subplot(1,2,1)
  plt.plot(epochs, loss, label = 'Training loss', c = 'b')
  plt.plot(epochs, val_loss, label = 'Validation loss', c = 'r')
  plt.title('Loss')
  plt.xlabel('Epochs')
  plt.legend();

  # Plot accuracy
  plt.subplot(1,2,2)
  plt.plot(epochs, accuracy, label = 'Training accuracy', c = 'b')
  plt.plot(epochs, val_accuracy, label = 'Validation accuracy', c = 'r')
  plt.title('Accuracy')
  plt.xlabel('Epochs')
  plt.legend();
