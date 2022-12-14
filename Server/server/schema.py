import graphene
import graphql_jwt
import db.schema.query as dbQuery
import db.schema.mutation as dbMutation


class Query(dbQuery.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    pass


class Mutation(dbMutation.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
