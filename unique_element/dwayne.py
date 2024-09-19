input = [1,6, 6, 2, 2, 3, 4, 4, 5]
list(set(input))

def unique_elements(input: list) -> list:
    ue_list = []
    for i in input:
        if i not in ue_list:
            ue_list.append(i)
    print(ue_list)

unique_elements(input)

# curious on the difference in python and JS syntax

# function uniqueElements(arr) {
#     let ueList = [];
#     for (let i = 0; i < arr.length; i++) {
#         if (!ueList.includes(arr[i])) {
#             ueList.push(arr[i]);
#         }
#     }
#     return ueList;
# }

# let arr = [1,4,5,6,7,8,4,3,1]
#console.lop(uniqueElements(arr))