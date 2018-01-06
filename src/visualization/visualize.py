import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

def plot_roc(fpr, tpr):
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(10,5))
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()


def plot_scatter(values, colors, ticks, ticks_labels):
    fig, axr = plt.subplots(figsize=(14, 5))
    cax = axr.scatter(values[:, 0], values[:, 1], c=colors, alpha=0.5)
    cbar = fig.colorbar(cax, ticks=ticks, orientation='vertical')
    cbar.ax.set_yticklabels(ticks_labels)
    plt.show()
