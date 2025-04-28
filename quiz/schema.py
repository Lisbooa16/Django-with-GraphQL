import graphene
from graphene_django import DjangoObjectType, DjangoListField

from users.models import ExtendUser
from .models import Quizzes, Category, Question, Answer
from django.db.models import ProtectedError
from graphql_auth.schema import UserQuery, MeQuery


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class UserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = '__all__'

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "quiz", "title")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "answer_text", "is_right")


class Query(UserQuery, MeQuery,  graphene.ObjectType):
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())
    # all_questions = graphene.List(QuestionType)

    def resolve_all_questions(root, info, id):
        return  Question.objects.get(pk=id)
    
    def resolve_all_answers(root, info, id):
        return  Answer.objects.filter(question=id)
    
    # def resolve_all_questions(root, info):
    #     return Question.objects.all()


# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
    
#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)

class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id, name):
        try:
            category = Category.objects.get(id=id)
            category.name = name
            category.save()
            return CategoryMutation(category=category)
        except Category.DoesNotExist:
            raise Exception('Impossivel criar por essa função')

class CategoryMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            category = Category.objects.get(id=id)
            category.delete()

            return CategoryMutationDelete(category=category)
        except:
            raise Exception("Não é possível excluir: a categoria está sendo usada.")
        
class CategoryMutationCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        try:
            category = Category.objects.create(name=name)
            category.save()

            return CategoryMutationCreate(category=category)
        except:
            raise Exception("Não é possível excluir: a categoria está sendo usada.")


class UserGet(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id):
        user = ExtendUser.objects.get(id=id)
        return UserGet(user=user)

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()
    delete_fields = CategoryMutationDelete.Field()
    create_category = CategoryMutationCreate.Field()

    # usuario

    pegar_usuario = UserGet.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)