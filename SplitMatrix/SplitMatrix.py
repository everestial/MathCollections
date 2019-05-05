
import numpy as np
#np.set_printoptions(precision=1)
import sys


def main():

    my_matrix = [[15, 10, 0, 0], [-10, 15, 10, 0],
                 [0, -10, 15, 10], [0, 0, 10, 15]]

    ## Use these code later !!! ******************
    #my_matrix = np.random.rand(40,40)
    #my_matrix = create_matrix(25)

    #id_matrix = [[1, 0, 0, 0], [0, 1, 0, 0],
     #            [0, 0, 1, 0], [0, 0, 0, 1]]
    ### ******************************************

    id_matrix = np.identity(len(my_matrix))
    print(id_matrix)
    print()

    #np.random.random_integers(3)
    #sys.exit(0)


    updated_matrix, checkers, contd = recursive_matrix_generator(my_matrix, id_matrix)

    print("\nMarker 01")
    print(updated_matrix)
    print(checkers)
    print(contd)
    #sys.exit(0)

    count = 0

    while contd == False:
        count = count + 1
        my_matrix = updated_matrix
        updated_matrix, checkers, contd = recursive_matrix_generator(my_matrix, id_matrix)
        print("nMarker %s" %(count))
        print(updated_matrix)
        print(checkers)
        print(contd)

    if contd == True:
        print("\nContd is True")
        print(checkers)
        zero_position_id = [True if abs(x) < 0.0001 else False for x in checkers]
        print(zero_position_id)
        zero_position_rc = [zero_position_id.index(True)+1, zero_position_id.index(True)]
        print(zero_position_rc)
        print()

        ### create new matrix blocks
        matrix_blck_01 = updated_matrix[:2,:2]
        matrix_blck_02 = updated_matrix[2:,2:]

        id_matrix_blck_01 = np.identity(len(matrix_blck_01))
        id_matrix_blck_02 = np.identity(len(matrix_blck_02))

        print(matrix_blck_01)
        print()
        print(matrix_blck_02)

        updated_matrix_blck_01 = recursive_matrix_generator(matrix_blck_01, id_matrix_blck_01)
        updated_matrix_blck_02 = recursive_matrix_generator(matrix_blck_02, id_matrix_blck_02)

        print("\nnew block matrix")
        print(updated_matrix_blck_01)
        print()
        print(updated_matrix_blck_02)

        ### ********* to be contd ..... - move while loop inside
        #### ******************************



def recursive_matrix_generator(my_matrix, id_matrix):
    # print(my_matrix)
    # find the multiplier by taking last value of the last row
    #multiplier = my_matrix[3][3]

    print(my_matrix)

    my_matrix_len = len(my_matrix)-1
    multiplier = my_matrix[my_matrix_len][my_matrix_len]

    shift_matrix = calc_shift_matrix(id_matrix, multiplier)
    #print('\nShift Matrix')
    #print(shift_matrix)

    new_matrix = calc_new_matrix(my_matrix, shift_matrix)

    q, r = calc_split_matrix(new_matrix)

    updated_matrix = update_matrix(q, r, shift_matrix)

    #print('\nUpdated Matrix')
    #print(updated_matrix)
    #print()
    #print(type(updated_matrix[0][2]))
    checkers, contd = make_checkers(updated_matrix)

    return updated_matrix, checkers, contd


def make_checkers(updated_matrix):
    max_val = len(updated_matrix)-1

    checkers = []
    for ath, bth in enumerate(range(max_val)):
        val = updated_matrix[ath+1][ath]
        checkers.append(val)

    ## old code for static enumeration
    #checkers = [updated_matrix[1][0], updated_matrix[2][1], updated_matrix[3][2]]

    checkers = [float(i) for i in checkers]
    contd = any(abs(i) < 0.0001 for i in checkers)

    return checkers, contd


def calc_shift_matrix(id_matrix, multiplier):
    # create a shift matrix
    shift_mat = []
    for lists in id_matrix:
        new_list = []
        for vals in lists:
            #print(new_mult*vals)
            new_list.append(multiplier*vals)
        shift_mat.append(new_list)

    return shift_mat


# now, update the matrix using the shift matrix
def calc_new_matrix(my_matrix, shift_matrix):
    new_matrix = []

    for ith, rows in enumerate(my_matrix):
        new_row = []
        for jth, value in enumerate(rows):
            new_value = my_matrix[ith][jth] - shift_matrix[ith][jth]
            new_row.append(new_value)

        new_matrix.append(new_row)

    print(new_matrix)
    print()
    return new_matrix


## testing split
def calc_split_matrix(new_matrix):
    #print("New matrix:")
    #print(new_matrix)
    qr_factor =  np.linalg.qr(new_matrix)

    #print("Decomposition of the said matrix:")
    q = qr_factor[0]
    r = qr_factor[1]

    return q, r


# matrix multiplication
def update_matrix(q, r, shift_matrix):
    new_m = np.dot(r, q)
    shift_matrix = np.array(shift_matrix)
    new_matrix = np.sum([new_m, shift_matrix], axis=0)

    return new_matrix


## Create a random matrix of specific size

def create_matrix(siz):
    from random import randint
    randint(100, 999)

    gen_matrix = []
    for xth in range(0,siz):
        gen_row = []
        for yth in range(0, siz):
            gen_row.append(randint(100, 999))
        gen_matrix.append(gen_row)

    return gen_matrix







if __name__ == '__main__':
    main()








