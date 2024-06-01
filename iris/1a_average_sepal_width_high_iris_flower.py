with open("../../../../Bai_Tap_Buoi_2/Iris.csv") as file:
    # Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species
    firt_line = file.readline()

    setosas = []    # array contain setosa flowers, each of element is an array, which has 6 elements
    versicolors = [] # array contain versicolor flowers, each of element is an array, which has 6 elements
    virginicas = [] # array contain virginica flowers, each of element is an array, which has 6 elements

    # count how many of each species flowers in Iris.csv sample file
    k_setosa = 0
    k_versicolor = 0
    k_virginica = 0

    # total sepal length, sepal width of each flower species
    total_setosas_sepal_length = 0
    total_setosas_sepal_width = 0
    total_versicolors_sepal_length = 0
    total_versicolors_sepal_width = 0
    total_virginicas_sepal_length = 0
    total_virginicas_sepal_width = 0
    # a dictionary has key, value including:
    # key: name of sepal_width, sepal_length of each species flowers
    # value: value of corresponding key
    average = {}

    for line in file:
        line_array = line.split(",")
        if line_array[5] == 'Iris-setosa\n':
            k_setosa += 1
            setosas.append(line_array)
        elif line_array[5] == 'Iris-versicolor\n':
            k_versicolor += 1
            versicolors.append(line_array)
        elif line_array[5] == 'Iris-virginica\n':
            k_virginica += 1
            virginicas.append(line_array)

    # calculate total sepal length and width of each specified iris flower
    for setosa in setosas:
        total_setosas_sepal_length += float(setosa[1])
        total_setosas_sepal_width += float(setosa[2])

    for versicolor in versicolors:
        total_versicolors_sepal_length += float(versicolor[1])
        total_versicolors_sepal_width += float(versicolor[2])

    for virginica in virginicas:
        total_virginicas_sepal_length += float(virginica[1])
        total_virginicas_sepal_width += float(virginica[2])

    # add paris or key and value to average dictionary
    average["average_setosas_sepal_length"] = total_setosas_sepal_length/ k_setosa
    average["average_setosas_sepal_width"] = total_setosas_sepal_width/ k_setosa
    average["average_versicolors_sepal_length"] = total_versicolors_sepal_length / k_versicolor
    average["average_versicolors_sepal_width"] = total_versicolors_sepal_width / k_versicolor
    average["average_virginicas_sepal_length"] = total_setosas_sepal_length / k_setosa
    average["average_virginicas_sepal_width"] = total_setosas_sepal_width / k_setosa

    # print average lenghth and with flowing key, value in dictionary of average above
    for key, value in average.items():
        print(f"{key}: {value}")



