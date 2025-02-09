from tkinter import *

def bubble(songs_list):
    root = Tk()
    root.title("최애곡 정렬기")
    root.geometry("640x360")

    list_length = len(songs_list) - 1
    i = 0

    while True:
        i += 1

        last_tried_result = songs_list[:]

        for j in range(list_length):
            # 기존 라벨 삭제 (중복 방지)
            for widget in root.winfo_children():
                widget.destroy()

            label_top = Label(root, text="버블 정렬")
            label_help = Label(root, text="둘 중 더 좋은 노래를 누르면 됩니다")
            label_sort_info = Label(root, text=f"{i} 회차, ({j + 1} / {list_length})번째 대결")
            label_top.pack()
            label_help.pack()
            label_sort_info.pack()

            result = IntVar(value=-1)

            button0 = Button(root, width=30, height=5, text=songs_list[j], command=lambda: result.set(0))
            button1 = Button(root, width=30, height=5, text=songs_list[j+1], command=lambda: result.set(1))
            button0.pack()
            button1.pack()

            # Button(root, width=15, height=3, text="누르면 꺼짐", command=root.destroy).pack()

            root.wait_variable(result)  # 버튼 클릭할 때까지 대기

            # print(result.get())
            if result.get() == 1:
                songs_list[j], songs_list[j+1] = songs_list[j+1], songs_list[j]
                print(f"{songs_list[j+1]}가 {songs_list[j]}의 뒤 ({j+2}번째 자리) 로 감. ")
        
        if last_tried_result == songs_list:
            root.destroy()
            break
        last_tried_result = songs_list[:]

    root.mainloop()

    return songs_list