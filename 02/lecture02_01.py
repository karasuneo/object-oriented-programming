#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from email.policy import strict
from itertools import count

def lecture02_01_printHeroStatus() -> None:
      hero_header = []
      hero_data = []
      with open('./csv/lecture02_Hero.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                  if len(hero_header) == 0:
                        hero_header = row
                  else :
                        hero_data.append(row)
                        
            
            for hero in hero_data :
                  if hero[0] == '1' :
                        hero_name = hero[1]
                        hero_hp = hero[2]
                        hero_mp = hero[3]
                        hero_atk = hero[4]
                        hero_def = hero[5]
                        hero_age = hero[6]
                        
      print(f"{hero_name}のステータスは" +
            f"HP:{hero_hp}," +
            f"MP:{hero_mp}," +
            f"Atk:{hero_atk}," +
            f"Def:{hero_def}," +
            f"Age:{hero_age}")

def lecture02_01_printWeaponStatus() -> None:
      count = 0
      weapon_header = []
      weapon_data = []
      with open('./csv/lecture02_Weapon.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                  if len(weapon_header) == 0:
                        weapon_header = row
                  else :
                        weapon_data.append(row)
                        
            for weapon in weapon_data :
                  if weapon[0] == '1' :
                        weapon_name = weapon[1]
                        weapon_hp = weapon[2]
                        weapon_mp = weapon[3]
                        weapon_atk = weapon[4]
                        weapon_def = weapon[5]
                        weapon_age = weapon[6]
                        
      print(f"{weapon_name}のステータスは" +
            f"HP:{weapon_hp}," +
            f"MP:{weapon_mp}," +
            f"Atk:{weapon_atk}," +
            f"Def:{weapon_def}," +
            f"Age:{weapon_age}")

def lecture02_01_printHeroStatusWithWeapon() -> None:
      weapon_header = []
      weapon_data = []
      hero_header = []
      hero_data = []
      with open('./csv/lecture02_Hero.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                  if len(hero_header) == 0:
                        hero_header = row
                  else :
                        hero_data.append(row)
      
      with open('./csv/lecture02_Weapon.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                  if len(weapon_header) == 0:
                        weapon_header = row
                  else :
                        weapon_data.append(row)
                        
            for hero in hero_data :
                  if hero[0] == '1' :
                        hero_name = str(hero[1])
                        hero_hp = int(hero[2])
                        hero_mp = int(hero[3])
                        hero_atk = int(hero[4])
                        hero_def = int(hero[5])
                        hero_age = int(hero[6])
                              
      
            for weapon in weapon_data :
                  if weapon[0] == '1' :
                        weapon_name = str(weapon[1])
                        weapon_hp = int(weapon[2])
                        weapon_mp = int(weapon[3])
                        weapon_atk = int(weapon[4])
                        weapon_def = int(weapon[5])
                        weapon_age = int(weapon[6])
                              
                              
      # # ステータス情報を出力する
      print(f"{weapon_name}を装備した{hero_name}のステータスは" +
      f"HP:{hero_hp+weapon_hp}," +
      f"MP:{hero_mp+weapon_mp}," +
      f"Atk:{hero_atk+weapon_atk}," +
      f"Def:{hero_def+weapon_def}," +
      f"Age:{hero_age+weapon_age}")

if __name__ == '__main__':
      lecture02_01_printHeroStatus()
      lecture02_01_printWeaponStatus()
      lecture02_01_printHeroStatusWithWeapon()