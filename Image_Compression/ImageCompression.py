import cv2
import matplotlib.pyplot as plt
import numpy as np 
from opencv_basics_grayscale import histogram_grayscale 
def histogram_color(image): 
    colors = ('b', 'g', 'r') 
    histograms = {} 
    for i, color in enumerate(colors): 
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        histograms[color] = hist.flatten()     
    return histograms 


def average_intensity(hist): 
    unique_colors=0 
    for i in range(256): 
        if hist[i] > 0: unique_colors += 1 
        return unique_colors 
    

def color_count(image_path): 
    image = cv2.imread(image_path) 
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    pixels = image_rgb.reshape(-1, 3) 
    unique_colors = set(map(tuple, pixels)) 
    return len(unique_colors) 


if __name__ == '__main__': 

    image1_location = 'flower.png' 

    img = cv2.imread(image1_location, cv2.IMREAD_GRAYSCALE) 
    img_color = cv2.imread(image1_location, cv2.IMREAD_COLOR) 

    jpeg_75_location = 'flower_75.jpg' 
    jpeg_50_location = 'flower_50.jpg' 
    jpeg_25_location = 'flower_25.jpg' 

    img_75_color = cv2.imread(jpeg_75_location, cv2.IMREAD_COLOR) 
    img_50_color = cv2.imread(jpeg_50_location, cv2.IMREAD_COLOR) 
    img_25_color = cv2.imread(jpeg_25_location, cv2.IMREAD_COLOR) 

    cv2.imwrite(jpeg_75_location, img, [cv2.IMWRITE_JPEG_QUALITY, 75]) 
    cv2.imwrite(jpeg_50_location, img, [cv2.IMWRITE_JPEG_QUALITY, 50]) 
    cv2.imwrite(jpeg_25_location, img, [cv2.IMWRITE_JPEG_QUALITY, 25]) 

    cv2.imwrite(jpeg_75_location, img_color, [cv2.IMWRITE_JPEG_QUALITY, 75]) 
    cv2.imwrite(jpeg_50_location, img_color, [cv2.IMWRITE_JPEG_QUALITY, 50]) 
    cv2.imwrite(jpeg_25_location, img_color, [cv2.IMWRITE_JPEG_QUALITY, 25]) 

    img_75 = cv2.imread(jpeg_75_location, cv2.IMREAD_GRAYSCALE) 
    img_50 = cv2.imread(jpeg_50_location, cv2.IMREAD_GRAYSCALE) 
    img_25 = cv2.imread(jpeg_25_location, cv2.IMREAD_GRAYSCALE) 

    hist_original = histogram_grayscale(img) 
    hist_75 = histogram_grayscale(img_75) 
    hist_50 = histogram_grayscale(img_50) 
    hist_25 = histogram_grayscale(img_25) 

    histograms_original = histogram_color(img_color) 
    histograms_original['gray'] = histogram_grayscale(img) 

    histograms_75 = histogram_color(img_75_color) 
    img_75_gray = cv2.cvtColor(img_75_color, cv2.COLOR_BGR2GRAY) 
    histograms_75['gray'] = histogram_grayscale(img_75_gray)

    histograms_50 = histogram_color(img_50_color) 
    img_50_gray = cv2.cvtColor(img_50_color, cv2.COLOR_BGR2GRAY) 
    histograms_50['gray'] = histogram_grayscale(img_50_gray) 

    histograms_25 = histogram_color(img_25_color) 
    img_25_gray = cv2.cvtColor(img_25_color, cv2.COLOR_BGR2GRAY) 
    histograms_25['gray'] = histogram_grayscale(img_25_gray)  

    labels = ['Original', 'JPEG 75%', 'JPEG 50%', 'JPEG 25%'] 
    colors = ['r', 'g', 'b', 'gray'] 
    color_labels = ['Red', 'Green', 'Blue', 'Gray'] 
    histograms = [histograms_original, histograms_25, histograms_50, histograms_75] 
    
    x = np.arange(len(labels)) 
    width = 0.2 

    fig, ax = plt.subplots() 
    for i, color in enumerate(colors): 
        intensities = [average_intensity(hist[color]) for hist in histograms] 
        ax.bar(x + (i * width), intensities, width, label=color_labels[i], color=color) 

    ax.set_xlabel('Image Quality') 
    ax.set_ylabel('Average Intensity') 
    ax.set_title('Average Intensity of Color Channels by Image Quality') 
    ax.set_xticks(x + width * 1.5) 
    ax.set_xticklabels(labels) 
    ax.legend() 

    fig.tight_layout() 
    plt.savefig("multi_bar_chart.png") 

    image_paths = ['flower.png', 'flower_75.jpg', 'flower_50.jpg','flower_25.jpg'] 
    color_counts = [(image_path, color_count(image_path)) for image_path in image_paths] 
    image_names, counts = zip(*color_counts) 


    plt.figure(figsize=(10, 6)) 
    plt.bar(image_names, counts, color='skyblue') 
    plt.xlabel('Image') 
    plt.ylabel('Unique Color Count') 
    plt.title('Unique Color Counts of Images') 
    plt.xticks(rotation=45) 
    plt.grid(axis='y', linestyle='--', alpha=0.7) 
    plt.tight_layout() 
    plt.savefig("color_count.png") 
    plt.show() 
    plt.close() 

    def plot_histograms(histograms, title, filename): 
        x = range(256) 
        plt.figure() 
        plt.plot(x, histograms['gray'], label='Grayscale', color='grey') 
        plt.plot(x, histograms['b'], label='Blue', color='blue') 
        plt.plot(x, histograms['g'], label='Green', color='green') 
        plt.plot(x, histograms['r'], label='Red', color='red') 
        plt.legend() 
        plt.title(title) 
        plt.xlabel("Pixel Value") 
        plt.ylabel("Frequency") 
        plt.savefig(filename) 
        plt.close() 
    
    
    plot_histograms(histograms_original, "Histogram - Original PNG", "histogram_original.png") 
    plot_histograms(histograms_75, "Histogram - JPEG 75% Quality", "histogram_75.png") 
    plot_histograms(histograms_50, "Histogram - JPEG 50% Quality", "histogram_50.png") 
    plot_histograms(histograms_25, "Histogram - JPEG 25% Quality", "histogram_25.png") 

    x = range(256) 
    plt.figure() 
    plt.plot(x, hist_original, label='Original PNG', color='black') 
    plt.plot(x, hist_25, label='JPEG 25%', color='grey') 
    plt.plot(x, hist_75, label='JPEG 75%', color='darkgrey') 
    plt.plot(x, hist_50, label='JPEG 50%', color='lightgrey') 
    plt.legend() 
    plt.title("Grayscale Histogram Comparison") 
    plt.xlabel("Pixel Value") 
    plt.ylabel("Frequency") 
    plt.savefig("grayscale_histogram_comparison.png") 
    plt.show() 
    plt.close()
