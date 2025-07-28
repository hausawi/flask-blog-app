from django.shortcuts import render
from django.http import HttpResponse


posts =[
    {
    
        'author': 'Haider',
        'title':'    بعض الجوانب الثقافية والتقليدية لشعوب الهوسا، التي تعكس ثراء وتنوع ثقافتهم في الفنون والترفيه.',
        'category':'التراث والثقافة',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here , making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'createdAt':'07:33 PM - 2025/05/17',
        'img':'/static/hausa2.png',
        'id': '01'
    },
    {
    
        'author': 'Haider',
        'title':'التطور الديني للشعب، بما في ذلك الأديان التقليدية والتحولات الدينية',
        'category':'الفكر والدين',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'createdAt':'07:33 PM - 2025/05/17',
        'img':'/static/hausa3.jpg',
        'id': '02'
    },

    {
    
        'author': 'Haider',
        'title':'الاقتصاد والتجارة والنشاط الاقتصادي للشعب، بما في ذلك الزراعة، والتجارة، والصناعة.',
        'category':'الاقتصاد والتجارة',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here , making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'createdAt':'07:33 PM - 2025/05/17',
        'img':'/static/hausa4.jpg',
        'id': '03'
    },
    {
    
        'author': 'Haider',
        'title':'الأصول والتاريخ المبكر و الأساطير والروايات الشفوية',
        'category':'الاصول والتاريخ',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'createdAt':'07:33 PM - 2025/05/17',
        'img':'/static/hausa1.jpg',
        'id': '04'
    },
    
]

def home(request):
    context ={
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})