from rich.console import Console
console = Console() 

name = input('Informe seu Nickname: ')

def logo(): 
      
      console.print ('''                             
 ______    ______     __    __    _____    __   ___
(_   _ \  (   __ \    ) )  ( (   / ____\  () ) / __)
  ) (_) )  ) (__) )  ( (    ) ) ( (___    ( (_/ /
  \   _/  (    __/    ) )  ( (   \___ \   ()   (
  /  _ \   ) \ \  _  ( (    ) )      ) )  () /\ | 
 _) (_) ) ( ( \ \_))  ) \__/ (   ___/ /   ( (  \ |
(______/   )_) \__/   \______/  /____/    ()_)  \_| 

                                        [white]Coded By[/]: Thor_kryp 
                                        [white]Version[/]: 1.0
''',style= "#AB14E1 bold") 

def bru(): 
  console.print(f"Hello, {name}!",style="on blue") 
  