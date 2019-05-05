import os
from filecmp import cmp


def create_num_of_random_files(number, base_path, desired_extension="txt", file_name="text_file"):
    for i in range(0, number):
        test_file_name = '%s%s.%s' % (file_name, str(i), desired_extension)
        with open(base_path + test_file_name, 'w') as f:
            f.write("This is a test file number %s. It will be deleted once the test is finished" % i)


def delete_num_of_randomly_create_files(number, base_path, desired_extension="txt", file_name="text_file"):
    for i in range(0, number):
        test_file_name = '%s%s.%s' % (file_name, str(i), desired_extension)
        os.remove(base_path + test_file_name)


def write_some_content_in_the_desired_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
        f.close()


def clear_the_content_of_the_desired_file(file_path):
    with open(file_path, 'w') as f:
        f.close()


def compare_two_lists(dict1, dict2):
    result = True
    for k in dict1:
        if k in dict2:
            if sorted(dict1[k]) == sorted(dict2[k]):
                continue
            else:
                result = False
                break
        else:
            result = False
            break
    return result
