from django.forms import ModelForm, TextInput, ValidationError
from funcionarios.models import Funcionario

class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['name', 'phone', 'email', 'city']
        widgets = {'phone': TextInput(attrs={'inputmode': 'numeric'}),}
        
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError('O campo deve ter pelo menos 3 caractes')
        return name
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        errors = []
            
        if phone[0] != '(': 
            if not errors: errors.append('Digite apenas números')
        if phone[3] != ')':
            if not errors: errors.append('Digite apenas números')
        if not phone[1:3].isdigit():
             if not errors: errors.append('Digite apenas números')
        if phone[10] != '-':
            if not errors: errors.append('Digite apenas números')
        if not phone[5:10].isdigit():
            if not errors: errors.append('Digite apenas números')
        if not phone[11:15].isdigit():   
            if not errors: errors.append('Digite apenas números')
            
        if len(phone) != 15:
            errors.append('O telefone digitado está incorreto')
        
        
        if errors:
            raise ValidationError(errors)
        
        return phone
        
        
        