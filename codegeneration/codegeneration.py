from codegeneration.functions import generate_code


if __name__ == '__main__':
    import os
    data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'data'))

    src1 = '{}/jobsdatastore.csv'.format(data_dir)
    src2 = '{}/jobsdatabucket.csv'.format(data_dir)
    #print (src1)
    generate_code(('jobsdatastore', src1),('jobsdatabucket', src2))
