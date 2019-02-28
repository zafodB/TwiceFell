'''
 * Created by filip on 28/02/2019
'''


def __init__():
    # f = open("a_example.txt", "r")
    f = open("d_pet_pictures.txt", "r")
    # f = open("d_pet_pic.txt", "r")

    number_photos = f.readline()

    photo_id_counter = 0

    master_dictionary = {}

    sorting_dictionary = {}

    slides_v_random = []

    for line in f:
        photo_data = line.split()

        number_tags = int(photo_data[1])

        tags = photo_data[-number_tags:]

        master_dictionary[photo_id_counter] = [photo_data[0], tags]
        photo_id_counter += 1

    # print(master_dictionary)

    def compare_photos_by_tags(photo_1, photo_2):
        different_tags_count = len(master_dictionary[photo_2][1])

        photo_1_tags = {}
        for tag in master_dictionary[photo_1][1]:
            photo_1_tags[tag] = None

        for tag in master_dictionary[photo_2][1]:
            if tag in photo_1_tags:
                different_tags_count -= 1
                # photo_1_tags.pop(tag)

        return different_tags_count + len(photo_1_tags)

    # print("different tags count is:  " + str(compare_photos_by_tags(1, 2)))

    def combine_verticals():
        # nonlocal sorting_dictionary

        sorting_dictionary = master_dictionary

        nonlocal slides_v_random

        for key in range(0, len(sorting_dictionary)):
            # print(type(sorting_dictionary[key][0]))
            if key not in sorting_dictionary:
                continue
            if sorting_dictionary[key][0] == "V":

                largest_difference = 0
                large_diff_id = False
                tries = 0

                if key > len(sorting_dictionary):
                    break

                for i in range(key, len(sorting_dictionary)):
                    if i in sorting_dictionary:
                        if tries > 5:
                            break
                        if sorting_dictionary[i][0] == "V":
                            current_difference = compare_photos_by_tags(key, i)

                            if current_difference > largest_difference:
                                largest_difference = current_difference
                                large_diff_id = i
                                tries += 1
                    else:
                        continue

                # print("The current photo being processed is: " + str(key) + " Largest difference is: " + str(
                #     largest_difference) +
                #       " and it is to this photo: " + str(large_diff_id))
                if large_diff_id:
                    slides_v_random.append([largest_difference, [key, large_diff_id]])

            # print("sup")

    def combine_verticals_horizontals(vertical_list):
        horizontal_list = []

        for key in range(0, len(master_dictionary)):

            # print(key)
            if master_dictionary[key][0] == "H":
                # print(master_dictionary[key][1])
                horizontal_list.append([key, len(master_dictionary[key][1])])

        vertical_list.extend(horizontal_list)
        return vertical_list

    combine_verticals()

    slides_v_random = combine_verticals_horizontals(slides_v_random)

    slides_unsorted = sorted(slides_v_random, key=lambda slide: slide[0])

    print(slides_unsorted)

__init__()
