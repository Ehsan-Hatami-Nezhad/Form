import tkinter
from tkinter import ttk
from tkinter import messagebox
import string

class Form(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Form")
        self.geometry(f"389x675-100+20")
        self.resizable(0,0)
    
    def submit_form(self):
        message=f"First Name:{self.first_name} , Last Name:{self.last_name} , Age:{self.age} , Gender:{self.gender_form()} , Soldier Status:{self.soldier_status_form()} , Height:{float(self.height)} , Weight:{float(self.weight)} , BMI:{self.bmi_form()} , Education:{self.education_form()} , Salary:{int(self.salary)} , Tax:{float(self.tax)} , Insurance:{float(self.insurance)} , Net Salary:{self.net_salary_form()} , Tel:{self.connections_tel()} , Email:{self.connections_email()}\n"
        with open("Personal.txt",mode="a+") as file1:
            file1.write(message)

    def net_salary_form(self):
        self.net_salary=float(self.salary) - float(self.tax)/100*float(self.salary) - float(self.insurance)/100*float(self.salary)
        return self.net_salary
    
    def active_soldier_status(self):
        if self.gender.get()==1:
            self.dropdown_soldier_status.config(state="active")
        else:
            self.dropdown_soldier_status.config(state="disabled")
            
    def gender_form(self):
        if self.gender.get()==1:
            return "Male"
        elif self.gender.get()==2:
            return "Female"
        elif self.gender.get()==3:
            return "Other"
    
    def education_form(self):
        if self.dropdown_education.get()=="Diploma":
            return "Diploma"
        elif self.dropdown_education.get()=="Bachelor":
            return "Bachelor"
        elif self.dropdown_education.get()=="Master":
            return "Master"
        elif self.dropdown_education.get()=="PH.D":
            return "PH.D"
    
    def soldier_status_form(self):
        if self.dropdown_soldier_status.get()=="Permanent exemption":
            return "Permanent exemption"
        elif self.dropdown_soldier_status.get()=="Educational exemption":
            return "Educational exemption"
        elif self.dropdown_soldier_status.get()=="Subject":
            return "Subject"
        elif self.dropdown_soldier_status.get()=="Absent":
            return "Absent"
        elif self.dropdown_soldier_status.get()=="Has a termination card":
            return "Has a termination card"
        else:
            return "-"

    def bmi_form(self):
        self.bmi=float(self.weight)/(float(self.height)**2)
        return ("{:.2f}".format(self.bmi)) 
    
    def active_connections_tel(self):
        if self.tel.get()==1:
            self.textbox_tel.config(state="normal")
        else:
            self.textbox_tel.config(state="disabled")
    
    def connections_tel(self):
        if self.tel.get()==1:
            self.textbox_tel.config(state="normal")
            return self.textbox_tel.get()
        else:
            self.textbox_tel.config(state="disabled")
            return "-"
    
    def connections_email(self):
        if self.email.get()==1:
            self.textbox_email.config(state="normal")
            return self.textbox_email.get()
        else:
            self.textbox_email.config(state="disabled")
            return "-"
    
    def active_connections_email(self):
        if self.email.get()==1:
            self.textbox_email.config(state="normal")
        else:
            self.textbox_email.config(state="disabled")
            
    def authentication_form(self):
        first_and_last_name_string=string.ascii_letters+" "
        self.first_name=self.textbox_first_name.get()
        authentication_first_and_last_name=all(character in first_and_last_name_string for character in self.first_name) and len(self.first_name)!=0 
        self.last_name=self.textbox_last_name.get()
        authentication_first_and_last_name=all(character in first_and_last_name_string for character in self.last_name) and len(self.last_name)!=0 
        age_digits=string.digits
        self.age=self.textbox_age.get()
        authentication_age=all(character in age_digits for character in self.age) and len(self.age)!=0 and int(self.age)>=0 and int(self.age)<=150
        authentication_gender=self.gender.get()==1 or self.gender.get()==2 or self.gender.get()==3
        height_and_weight_digits=string.digits+"."
        self.height=self.textbox_height.get()
        authentication_height=all(character in height_and_weight_digits for character in self.height) and len(self.height)>0 and float(self.height)>0 and float(self.height)<=2.20 and self.height[0]!="." and self.height[-1]!="." and self.height.count(".")<=1
        self.weight=self.textbox_weight.get()
        authentication_weight=all(character in height_and_weight_digits for character in self.weight) and len(self.weight)>0 and float(self.weight)>=0 and float(self.weight)<=200 and self.weight[0]!="." and self.weight[-1]!="." and self.weight.count(".")<=1
        authentication_education=self.dropdown_education.get()=="Diploma" or self.dropdown_education.get()=="Bachelor" or self.dropdown_education.get()=="Master" or self.dropdown_education.get()=="PH.D"
        self.salary=self.textbox_salary.get()
        authentication_salary=all(character in age_digits for character in self.salary) and len(self.salary)>0 and int(self.salary)>0
        self.tax=self.textbox_tax.get()
        authentication_tax=all(character in height_and_weight_digits for character in self.tax) and len(self.tax)>0 and float(self.tax)>=0 and float(self.tax)<=100 and self.tax[0]!="." and self.tax[-1]!="." and self.tax.count(".")<=1
        self.insurance=self.textbox_insurance.get()
        authentication_insurance=all(character in height_and_weight_digits for character in self.insurance) and len(self.insurance)>0 and float(self.insurance)>=0 and float(self.insurance)<=100 and self.insurance[0]!="." and self.insurance[-1]!="." and self.insurance.count(".")<=1
        authentication_insurance_and_tax=len(self.insurance)!=0 and len(self.tax)!=0 and (float(self.insurance)+float(self.tax))>=0 and (float(self.insurance)+float(self.tax))<=100
        self.tel_f=self.textbox_tel.get()
        authentication_tel=all(character in age_digits for character in self.tel_f) and len(self.tel_f)==11 
        self.email_f=self.textbox_email.get()
        authentication_email = len(self.email_f)!=0
        
        if self.tel.get()==1 and self.email.get()==0:      
            if authentication_first_and_last_name and authentication_age and authentication_gender and authentication_height and authentication_weight and authentication_education and authentication_salary and authentication_tax and authentication_insurance and authentication_insurance_and_tax and authentication_tel:
                self.btn_submit.config(state="normal")
            else:
                message_error="You Should Edit :\n"
                if authentication_first_and_last_name==False:
                    message_error+="FirstName or LastName\n"
                if authentication_age==False:
                    message_error+="Age\n"
                if authentication_gender==False:
                    message_error+="Gender\n"
                if authentication_height==False:
                    message_error+="Height\n"
                if authentication_weight==False:
                    message_error+="Weight\n"
                if authentication_education==False:
                    message_error+="Education\n"
                if authentication_salary==False:
                    message_error+="Salary\n"
                if authentication_tax==False:
                    message_error+="Tax\n"
                if authentication_insurance==False:
                    message_error+="Insurance\n"
                if authentication_insurance_and_tax==False:
                    message_error+="Insurance + Tax = 100\n"
                if authentication_tel==False:
                    message_error+="Tel"
                messagebox.showerror("Error",message_error)
        elif self.tel.get()==0 and self.email.get()==1:
            if authentication_first_and_last_name and authentication_age and authentication_gender and authentication_height and authentication_weight and authentication_education and authentication_salary and authentication_tax and authentication_insurance and authentication_insurance_and_tax and authentication_email:
                self.btn_submit.config(state="normal")
            else:
                message_error="You Should Edit :\n"
                if authentication_first_and_last_name==False:
                    message_error+="FirstName or LastName\n"
                if authentication_age==False:
                    message_error+="Age\n"
                if authentication_gender==False:
                    message_error+="Gender\n"
                if authentication_height==False:
                    message_error+="Height\n"
                if authentication_weight==False:
                    message_error+="Weight\n"
                if authentication_education==False:
                    message_error+="Education\n"
                if authentication_salary==False:
                    message_error+="Salary\n"
                if authentication_tax==False:
                    message_error+="Tax\n"
                if authentication_insurance==False:
                    message_error+="Insurance\n"
                if authentication_insurance_and_tax==False:
                    message_error+="Insurance + Tax = 100\n"
                if authentication_email==False:
                    message_error+="Email"
                messagebox.showerror("Error",message_error)
        
        elif self.tel.get()==1 and self.email.get()==1:
            if authentication_first_and_last_name and authentication_age and authentication_gender and authentication_height and authentication_weight and authentication_education and authentication_salary and authentication_tax and authentication_insurance and authentication_insurance_and_tax and authentication_email and authentication_tel:
                self.btn_submit.config(state="normal")
            else:
                message_error="You Should Edit :\n"
                if authentication_first_and_last_name==False:
                    message_error+="FirstName or LastName\n"
                if authentication_age==False:
                    message_error+="Age\n"
                if authentication_gender==False:
                    message_error+="Gender\n"
                if authentication_height==False:
                    message_error+="Height\n"
                if authentication_weight==False:
                    message_error+="Weight\n"
                if authentication_education==False:
                    message_error+="Education\n"
                if authentication_salary==False:
                    message_error+="Salary\n"
                if authentication_tax==False:
                    message_error+="Tax\n"
                if authentication_insurance==False:
                    message_error+="Insurance\n"
                if authentication_insurance_and_tax==False:
                    message_error+="Insurance + Tax = 100\n"
                if authentication_tel==False:
                    message_error+="Tel\n"
                if authentication_email==False:
                    message_error+="Email"
                messagebox.showerror("Error",message_error)
        
        elif self.tel.get()==0 and self.email.get()==0:
            if authentication_first_and_last_name and authentication_age and authentication_gender and authentication_height and authentication_weight and authentication_education and authentication_salary and authentication_tax and authentication_insurance and authentication_insurance_and_tax:
                self.btn_submit.config(state="normal")
            else:
                message_error="You Should Edit :\n"
                if authentication_first_and_last_name==False:
                    message_error+="FirstName or LastName\n"
                if authentication_age==False:
                    message_error+="Age\n"
                if authentication_gender==False:
                    message_error+="Gender\n"
                if authentication_height==False:
                    message_error+="Height\n"
                if authentication_weight==False:
                    message_error+="Weight\n"
                if authentication_education==False:
                    message_error+="Education\n"
                if authentication_salary==False:
                    message_error+="Salary\n"
                if authentication_tax==False:
                    message_error+="Tax\n"
                if authentication_insurance==False:
                    message_error+="Insurance\n"
                if authentication_insurance_and_tax==False:
                    message_error+="Insurance + Tax = 100"
                messagebox.showerror("Error",message_error)

    def clear_form(self):
        self.textbox_first_name.delete(0,tkinter.END)
        self.textbox_last_name.delete(0,tkinter.END)
        self.textbox_age.delete(0,tkinter.END)
        self.textbox_height.delete(0,tkinter.END)
        self.textbox_weight.delete(0,tkinter.END)
        self.textbox_salary.delete(0,tkinter.END)
        self.textbox_tax.delete(0,tkinter.END)
        self.textbox_insurance.delete(0,tkinter.END)
        self.textbox_tel.delete(0,tkinter.END)
        self.textbox_email.delete(0,tkinter.END)
        self.gender.set(0)
        self.tel.set(0)
        self.email.set(0)
        self.dropdown_soldier_status.set("-------------------------------")
        self.dropdown_education.set("-------------------------------")
        self.btn_submit.config(state="disabled")
        self.textbox_tel.config(state="disabled")
        self.textbox_tel.delete(0,tkinter.END)
        self.textbox_email.config(state="disabled")
        self.textbox_email.delete(0,tkinter.END)
        self.textbox_first_name.focus()
    
    def create_widgets(self):
        self.lable_first_name=tkinter.Label(self,text="First Name:",font=("Arial",15,"bold"))
        self.lable_last_name=tkinter.Label(self,text="Last Name:",font=("Arial",15,"bold"))
        self.lable_age=tkinter.Label(self,text="Age:",font=("Arial",15,"bold"))
        self.lable_gender=tkinter.Label(self,text="Gender:",font=("Arial",15,"bold"))
        self.lable_soldier_status=tkinter.Label(self,text="Soldier Status:",font=("Arial",15,"bold"))
        self.lable_height=tkinter.Label(self,text="Height(m):",font=("Arial",15,"bold"))
        self.lable_weight=tkinter.Label(self,text="Weight(kg):",font=("Arial",15,"bold"))
        self.lable_BMI=tkinter.Label(self,text="BMI:",font=("Arial",15,"bold"))
        self.lable_education=tkinter.Label(self,text="Education:",font=("Arial",15,"bold"))
        self.lable_salary=tkinter.Label(self,text="Salary:",font=("Arial",15,"bold"))
        self.lable_tax=tkinter.Label(self,text="Tax(%):",font=("Arial",15,"bold"))
        self.lable_insurance=tkinter.Label(self,text="Insurance(%):",font=("Arial",15,"bold"))
        self.lable_net_salary=tkinter.Label(self,text="Net Salary:",font=("Arial",15,"bold"))
        self.lable_connections=tkinter.Label(self,text="Connections:",font=("Arial",15,"bold"))
        self.lable_tel=tkinter.Label(self,text="Tel:",font=("Arial",15,"bold"))
        self.lable_email=tkinter.Label(self,text="Email:",font=("Arial",15,"bold"))
        self.textbox_first_name=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_first_name.focus()
        self.textbox_last_name=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_age=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_height=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_weight=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_BMI=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid",state="disabled")
        self.textbox_salary=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_tax=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_insurance=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid")
        self.textbox_net_salary=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid",state="disabled")
        self.textbox_tel=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid",state="disabled")
        self.textbox_email=tkinter.Entry(self,font=("Arial",15,"italic"),relief="solid",state="disabled")
        self.gender=tkinter.IntVar()
        self.radio_male=tkinter.Radiobutton(self,text="Male",variable=self.gender,value=1,font=("Arial",12,"italic"),command=self.active_soldier_status)
        self.radio_female=tkinter.Radiobutton(self,text="Female",variable=self.gender,value=2,font=("Arial",12,"italic"),command=self.active_soldier_status)
        self.radio_other=tkinter.Radiobutton(self,text="Other",variable=self.gender,value=3,font=("Arial",12,"italic"),command=self.active_soldier_status)
        self.gender.set(0)
        self.dropdown_soldier_status=ttk.Combobox(self,values=["Permanent exemption","Educational exemption","Subject","Absent","Has a termination card"],state="disabled",font=("Arial",13,"italic"),width=23)
        self.dropdown_soldier_status.set("-------------------------------")
        self.dropdown_education=ttk.Combobox(self,values=["Diploma","Bachelor","Master","PH.D"],font=("Arial",13,"italic"),width=23)
        self.dropdown_education.set("-------------------------------")
        self.tel=tkinter.IntVar()
        self.email=tkinter.IntVar()
        self.checkbox_tel=tkinter.Checkbutton(self,variable=self.tel,text="Tel",command=self.active_connections_tel,font=("Arial",12,"italic"),onvalue=1,offvalue=0)
        self.checkbox_email=tkinter.Checkbutton(self,variable=self.email,text="Email",command=self.active_connections_email,font=("Arial",12,"italic"),onvalue=1,offvalue=0)
        self.btn_authentication=tkinter.Button(self,text="Authenticat",fg="#000",relief="solid",bg="#fff",font=("Arial",12,"italic"),width=15,command=self.authentication_form)
        self.btn_submit=tkinter.Button(self,text="Submit",fg="#000",relief="solid",bg="#fff",font=("Arial",12,"italic"),width=10,state="disabled",command=self.submit_form)
        self.btn_clear=tkinter.Button(self,text="Clear",fg="#000",relief="solid",bg="#fff",font=("Arial",12,"italic"),width=10,command=self.clear_form)

    def locate_widgets(self):
        self.lable_first_name.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.lable_last_name.grid(row=1,column=0,padx=5,pady=5,sticky="w")
        self.lable_age.grid(row=2,column=0,padx=5,pady=5,sticky="w")
        self.lable_gender.grid(row=3,column=0,padx=5,pady=5,sticky="w")
        self.lable_soldier_status.grid(row=4,column=0,padx=5,pady=5,sticky="w")
        self.lable_height.grid(row=5,column=0,padx=5,pady=5,sticky="w")
        self.lable_weight.grid(row=6,column=0,padx=5,pady=5,sticky="w")
        self.lable_BMI.grid(row=7,column=0,padx=5,pady=5,sticky="w")
        self.lable_education.grid(row=8,column=0,padx=5,pady=5,sticky="w")
        self.lable_salary.grid(row=9,column=0,padx=5,pady=5,sticky="w")
        self.lable_tax.grid(row=10,column=0,padx=5,pady=5,sticky="w")
        self.lable_insurance.grid(row=11,column=0,padx=5,pady=5,sticky="w")
        self.lable_net_salary.grid(row=12,column=0,padx=5,pady=5,sticky="w")
        self.lable_connections.grid(row=13,column=0,padx=5,pady=5,sticky="w")
        self.lable_tel.grid(row=14,column=0,padx=5,pady=5,sticky="w")
        self.lable_email.grid(row=15,column=0,padx=5,pady=5,sticky="w")
        self.textbox_first_name.grid(row=0,column=1,pady=5,columnspan=3)
        self.textbox_last_name.grid(row=1,column=1,pady=5,columnspan=3)
        self.textbox_age.grid(row=2,column=1,pady=5,columnspan=3)
        self.textbox_height.grid(row=5,column=1,pady=5,columnspan=3)
        self.textbox_weight.grid(row=6,column=1,pady=5,columnspan=3)
        self.textbox_BMI.grid(row=7,column=1,pady=5,columnspan=3)
        self.textbox_salary.grid(row=9,column=1,pady=5,columnspan=3)
        self.textbox_tax.grid(row=10,column=1,pady=5,columnspan=3)
        self.textbox_insurance.grid(row=11,column=1,pady=5,columnspan=3)
        self.textbox_net_salary.grid(row=12,column=1,pady=5,columnspan=3)
        self.textbox_tel.grid(row=14,column=1,pady=5,columnspan=3)
        self.textbox_email.grid(row=15,column=1,pady=5,columnspan=3)
        self.radio_male.grid(row=3,column=1,pady=5)
        self.radio_female.grid(row=3,column=2,pady=5)
        self.radio_other.grid(row=3,column=3,pady=5)
        self.dropdown_soldier_status.grid(row=4,column=1,pady=5,columnspan=3)
        self.dropdown_education.grid(row=8,column=1,pady=5,columnspan=3)
        self.checkbox_tel.grid(row=13,column=1,pady=5)
        self.checkbox_email.grid(row=13,column=2,pady=5)
        self.btn_authentication.grid(row=16,column=0,padx=5)
        self.btn_submit.grid(row=16,column=1,padx=5,columnspan=2,sticky="w")
        self.btn_clear.grid(row=16,column=2,columnspan=2,sticky="e")
        
    def show_form(self):
        self.mainloop()

my_form=Form()
my_form.create_widgets()
my_form.locate_widgets()
my_form.show_form()