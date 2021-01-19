import pandas as pd
import matplotlib.pyplot as plt


class DataDecoder :
    def __init__(self, name):
        self.name = name
        self.dataframe =  None
        self.fileData = None
        self.Data = []
        self.channels = ["yoc_temp", 'yoc_SP', 'yoc_p1', 'yoc_p2',
                        'yoc_p3', 'yoc_p4', 'yoc_p5', 'yoc_bl1','yoc_bl2',
                        'yoc_lights', 'yoc_stereo', 'yoc_h1', 'yoc_h2',
                        'yoc_filter', 'yoc_bl3', 'yoc_bl4', 'yoc_bl5','yoc_bl6',
                        'yoc_h_adc', 'yoc_bl7', 'yoc_econ', 'yoc_i_adc',
                        'yoc_all_on', 'yoc_bl8', 'yoc_bl9', 'yoc_bl10']

    def __read(self):
        """
        method to read the logger file
        """
        with open(self.name , "r") as f:
            self.fileData = f.readlines()

    def __ExtractData(self):
        """
        putting each line in a list and putting them into a list
        """
        for l in self.fileData:
            # we don't take the last element because it's the new line
            #(last ,is end of line) we also leave the time and the yoc_live out
            line_list = l.split(",")[2:-1]
            self.Data.append(line_list)
    def __CreateDataFrame(self):
        """
        Creates a panda dataframe from the data
        """
        self.dataframe = pd.DataFrame(self.Data , columns = self.channels)
    def __ConvertHexToDec(self):
        """
        convert from hexadecimal into decimal
        """
        for i in self.channels:
            self.dataframe[i] = self.dataframe.apply(lambda x: int(x[i] , 16) , axis = 1)


    def __PlotOne(self):
        """
        plotting the first plot
        yoc_temp, yoc_SP, yoc_SP,yoc_h_adc, yoc_h1,yoc_h2,
        """
        fig1, axes = plt.subplots()
        sx = axes.twinx()
        axes.plot(self.dataframe.index , self.dataframe["yoc_temp"], label="yoc_temp")
        axes.plot(self.dataframe.index , self.dataframe["yoc_SP"] , label="yoc_SP")
        axes.plot(self.dataframe.index , self.dataframe["yoc_h_adc"], label="yoc_h_adc")
        sx.plot(self.dataframe.index, self.dataframe["yoc_h1"] , label="yoc_h1")
        axes.plot(self.dataframe.index , self.dataframe["yoc_h2"] , label="yoc_h2")
        plt.show()
    def __PlotTwo(self):
        """
        Plotting the 2nd plot
        yoc_p1 till yoc_p5, yoc_i_adc,
        """
        fig2, axes = plt.subplots()
        sx = axes.twinx()
        axes.plot(self.dataframe.index, self.dataframe["yoc_p1"], label="yoc_p1")
        axes.plot(self.dataframe.index, self.dataframe["yoc_p2"], label="yoc_p2")
        axes.plot(self.dataframe.index, self.dataframe["yoc_p3"], label="yoc_p3")
        axes.plot(self.dataframe.index, self.dataframe["yoc_p4"], label="yoc_p4")
        axes.plot(self.dataframe.index, self.dataframe["yoc_p5"], label="yoc_p5")
        sx.plot(self.dataframe.index, self.dataframe["yoc_i_adc"], label="yoc_i_adc")
        plt.show()
    def __PlotThree(self):
        """
        plotting third plots
        yoc_filter,yoc_h1 ,yoc_h2, yoc_i_adc
        """
        fig3, axes = plt.subplots()
        sx = axes.twinx()
        axes.plot(self.dataframe.index, self.dataframe[f"yoc_filter"], label="yoc_filter")
        axes.plot(self.dataframe.index , self.dataframe["yoc_h1"] , label="yoc_h1")
        axes.plot(self.dataframe.index, self.dataframe["yoc_h2"] , label="yoc_h2")
        sx.plot(self.dataframe.index, self.dataframe["yoc_i_adc"], label="yoc_i_adc")
        plt.show()
    def __convertCSV(self , FileName):
        """
        Converts the dataframe to a csv file
        """

        self.dataframe.to_csv(f"{FileName}.csv", index=True)

    def DecodeAndConverttoCSV(self , FileName):
        self.__read()
        self.__ExtractData()
        self.__CreateDataFrame()
        self.__ConvertHexToDec()
        self.__convertCSV(FileName)
    def Ploting(self):
        self.__PlotOne()
        self.__PlotTwo()
        self.__PlotThree()


x = DataDecoder("outputfile.txt")
x.DecodeAndConverttoCSV("DATA")
x.Ploting()
