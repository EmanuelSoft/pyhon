command=""
started=False
stoped=False
while command!="quit":
      command=input(">").lower()
      if command=="help":
        print("start- to tart the car")
        print("stop -to stop the car")
        print("quit -to exit")
      elif command=="start":
            if started:
             print("the car is already started...")
            else:
              started=True
              print("car started...")   
      elif command=="stop":
          if not stoped:
             print("car is aready stopped")
          else:
             started=False
             print("car stopped")
      elif command=="quit":
          break  
      else:
        print("sorry i don't understand this")
   
   