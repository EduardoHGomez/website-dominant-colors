# import libraries: pandas, sckit
from imports import  *

def get_dominant_colors(image_address, k):
    # Get image as array of size M * N (Size in pixels) and RGB
    image = img.imread(image_address)

    # Construct the dataframe
    df = pd.DataFrame()
    df['r']=pd.Series(image[:,:,0].flatten())
    df['g']=pd.Series(image[:,:,1].flatten())
    df['b']=pd.Series(image[:,:,2].flatten())

    '''
    Since the data will be between 0-255 it can actually be
    standarized, otherwise we would want the punishment to
    be larger but not for this case, that's what withen is used
    '''
    df['r_whiten'] = whiten(df['r'])
    df['g_whiten'] = whiten(df['g'])
    df['b_whiten'] = whiten(df['b'])

    # K means algorithm from scikit
    cluster_centers, distortion = kmeans(df[['r_whiten', 'g_whiten', 'b_whiten']], k)

    # Get colors back sto RGB
    r_std, g_std, b_std = df[['r', 'g', 'b']].std()
    colors=[]
    for color in cluster_centers:
        sr, sg, sb = color
        colors.append((int(sr*r_std), int(sg*g_std), int(sb*b_std)))
    
    # Conver to hex format
    code_of_colors = list()
    for color in colors:
        hex_value = '#{:02x}{:02x}{:02x}'.format(*color)
        code_of_colors.append(hex_value)

    return code_of_colors

if __name__ == "__main__":
    get_dominant_colors()

