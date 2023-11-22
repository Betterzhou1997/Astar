import numpy as np
import matplotlib.pyplot as plt

def show_step_img(data, step):
    data = np.array(data)
    plt.imshow(data, interpolation='nearest', vmin=0, vmax=1)  # 使用viridis颜色映射
    plt.axis('off')
    # 在图中添加对应的数字
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            plt.text(j, i, str(data[i, j]), ha='center', va='center', fontsize=30, color='black')
    plt.title(f'STEP: {step}', fontsize=20, )
    plt.savefig(f'img/step{step}.png')
    plt.show()


