from libgreader import GoogleReader, ClientAuthMethod, Feed
auth = ClientAuthMethod('acpigeon', 'Katana666')
reader = GoogleReader(auth)
print reader.getUserInfo()

