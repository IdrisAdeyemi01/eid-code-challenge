def shuffleClass(students, numToMove):
    '''
    This function takes in two arguments:
    students - This is a list of numbers to be shuffled
    numToMove - This is the number to which the students' list is shifted    
    '''
    assert type(students)== list and type(numToMove)== int, 'The students should be a list and numToMove, an integer'
    assert len(students) > 0, 'The students list should not be an empty list'
    for i in students:
        assert type(i) == int, 'The list of students should only contain integers'
    if numToMove > len(students):
        numToMove = (numToMove % len(students)-1) + 1
    if numToMove == 0:
        return students
    else:
        shiftedArr = students[0:numToMove+1]
        
        students = students[numToMove+1::]

        newArray = students + shiftedArr
        
        return newArray
