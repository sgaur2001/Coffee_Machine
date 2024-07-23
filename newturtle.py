import turtle as t
timmy=t.Turtle()
def draw_size(num_side):
    for i in range(num_side):
        angle=360/num_side
        timmy.forward(100)
        timmy.right(angle)

for shap_side_n in range(3,11):
    draw_size(shap_side_n)
