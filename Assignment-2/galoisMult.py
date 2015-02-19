import os
import commands

list_1 = ["02", "03", "01", "01"]
list_2 = ["01", "02", "03", "01"]
list_3 = ["01", "01", "02", "03"]
list_4 = ["03", "01", "01", "02"]

input_vector_1 = ["E5", "E4", "59", "EB"]
input_vector_2 = ["F3", "68", "84", "47"]
input_vector_3 = ["59", "8A", "59", "24"]
input_vector_4 = ["47", "F3", "B5", "C4"]

def galois_mult(row, input_vector):

        #input_vector = ["16", "16", "16", "16"]
        output_list = []
        for i in xrange(0, len(row)):

            num1 = int(row[i], 16)
            num2 = int(input_vector[i], 16)
            status, output = commands.getstatusoutput("./gf_mult "+str(num1) +" " + str(num2) + " 8")
            output_list.append(output)
            print hex(int(output)).split('x')[1]

        status, output1 = commands.getstatusoutput("./gf_xor "+ str(output_list[0]) +" " + str(output_list[1]))
        status, output2 = commands.getstatusoutput("./gf_xor "+ str(output_list[2]) +" " + str(output_list[3]))
        status, output = commands.getstatusoutput("./gf_xor "+ str(output1) +" " + str(output2))
        print hex(int(output)).split('x')[1] + " ",

print "Column 1:",
galois_mult(list_1, input_vector_1)
galois_mult(list_2, input_vector_1)
galois_mult(list_3, input_vector_1)
galois_mult(list_4, input_vector_1)


print "\nColumn 2",
galois_mult(list_1, input_vector_2)
galois_mult(list_2, input_vector_2)
galois_mult(list_3, input_vector_2)
galois_mult(list_4, input_vector_2)


print "\nColumn 3:",
galois_mult(list_1, input_vector_3)
galois_mult(list_2, input_vector_3)
galois_mult(list_3, input_vector_3)
galois_mult(list_4, input_vector_3)

print "\nColumn 4:",
galois_mult(list_1, input_vector_4)
galois_mult(list_2, input_vector_4)
galois_mult(list_3, input_vector_4)
galois_mult(list_4, input_vector_4)
