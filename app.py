
from pywebio.input import input, FLOAT,input_group,textarea
from pywebio.output import put_text,put_warning,put_success


def bmi_app():
    name=input("Whats Your name")
    put_text('Hi, welcome to our website', name)

    user_info=input_group("User_info",[input('Whats Your age?', name='age',type=FLOAT)
                                ])
    if user_info['age']<16:
        put_warning("Sorry You can't access our website, Your age is less than 16")
    else:
        put_success('Congrats, You can use our website!')
        
        height = input("Input your height(cm)：", type=FLOAT)
        weight = input("Input your weight(kg)：", type=FLOAT)

        BMI = weight / (height / 100) ** 2

        top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

        for top, status in top_status:
            if BMI <= top:
                put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
                break
        
        

    
if __name__ == '__main__':
    bmi_app()