import urllib.request

url = "https://myjobstreet.jobstreet.com.my/application/application-status.php?view=1&action=aca&x=08p0di9qc8p5u2tguh6vqou7m6"
infile = urllib.request.urlopen(url) # Open the URL
data = infile.read().decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1

print(data) # Print the data to the screen