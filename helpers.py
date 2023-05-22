# import libraries: pandas, sckit
from imports import  *

def get_dominant_colors(image_address):
    # Get image as array of size M * N (Size in pixels) and RGB
    image = img.imread('sample1.jpg')

    # Construct the dataframe
    df = pd.DataFrame()
    df['r']=pd.Series(image[:,:,0].flatten())
    df['g']=pd.Series(image[:,:,1].flatten())
    df['b']=pd.Series(image[:,:,2].flatten())

    # Standarize data
    df['r_whiten'] = whiten(df['r'])
    df['g_whiten'] = whiten(df['g'])
    df['b_whiten'] = whiten(df['b'])

    # Apply k means algorithm from sckit and standarized data
    k = 4
    cluster_centers, distortion = kmeans(df[['r_whiten', 'g_whiten', 'b_whiten']], k)

    # Get colors backto RGB
    r_std, g_std, b_std = df[['r', 'g', 'b']].std()
    colors=[]
    for color in cluster_centers:
        sr, sg, sb = color
        colors.append((int(sr*r_std), int(sg*g_std), int(sb*b_std)))
    
    print(colors)
    
    # Display colors:
    #plt.imshow([colors])
    #plt.show()

    return colors

if __name__ == "__main__":
    get_dominant_colors()

