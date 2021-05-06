#연결리스트를 이용한 전화번호부 자료관리

class Node():
    def __init__(self):
        self.data = None #노드의 데이터 값
        self.link = None #먼저 저장된 앞의 노드를 가리킨다.


def printStack(top): #스택의 노드들을 top이 가리키는 마지막 노드부터 맨 처음에 저장된 노드까지 출력
    print('\n스택 자료 :\n')
    current = top
    if current == None: #빈 스택이므로 그냥 리턴
        return
    if current.link == None:
        print(current.data, end=' ')
    else :
        print(current.data, '->', end = ' ')
    while current.link != None: #앞 노드가 있는 동안
        current = current.link 
        if current.link ==None: #마지막 노드에는 화살표가 붙지 않는다.
            print(current.data, end = ' ')
        else :
            print(current.data, '->', end = ' ')
    print('\n\n')


def pop(top):
#top 변수가 가리키는 노드의 값을 스택에서 삭제하고 그 값을 반환한다.
    if top == None : #빈 스택
        print("빈 스택입니다.")
        return top

    delete_node = top # top 변수가 가리키는 맨 마지막 노드를 삭제하는 것이고
    top = top.link #top 변수는 그 앞의 노드를 가리키게 된다.
    print("%s pop 완료\n" %delete_node)
    del(delete_node) #해당 노드를 삭제
    return top #변경된 top 값을 반환한다.

                       

def push(top, new_data):
#새 노드를 스택의 마지막 노드로 연결
    node = Node()
    node.data = new_data

    if top == None: #빈 스택
        top = node #노드를 첫 번째 노드로 하고, 이 노드를 이제 top이 가리킨다.
        return top

    node.link = top #기존에 top 변수가 가리키던 노드를 새 노드가 가리키게 한다.
    top = node #top이 새 노드를 가리킨다.
    return top

    
if __name__=="__main__":

    top = None

    print('연결리스트를 이용한 스택구현 프로그램입니다.\n')

    while True:
        print('\n1: push\t 2:pop\t 3:출력\t 0:종료\n')
        
        ch = input("기능 선택--> ")
            
        if ch == '0':
            print('종료합니다\n')
            break

        elif ch == '1':
            add_data = (input('입력할 자료: '))
            
            top = push(top, add_data)
            printStack(top)

        elif ch == '2':
            top = pop(top)
            printStack(top)

        elif ch ==  '3':
            printStack(top)
            
        else:       
            print('\n잘못된 입력입니다.\n')
