import matplotlib.pyplot as plt
def saveplot(name,app='.pdf'):
    plt.savefig("../../../report/img/" + name + app)