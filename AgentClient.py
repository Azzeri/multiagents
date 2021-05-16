class AgentClient:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def returnalbums(data_sets, maxprice, minprice, agents_seller):
        albums_to_return = []
        for agent in agents_seller:
            albums_from_seller = agent.returnalbums(data_sets)
            for album in albums_from_seller:
                if float(maxprice) >= float(album.price) >= float(minprice):
                    albums_to_return.append(album)

        return albums_to_return
