import { Component, OnInit } from '@angular/core';
import { DataService } from '../db.service';
import { Router } from '@angular/router';
import { Restaurant } from '../dto/restaurant';
import { Mall } from '../dto/mall';

@Component({
  selector: 'app-restaurant',
  templateUrl: './restaurant.component.html',
  styleUrls: ['./restaurant.component.css']
})
export class RestaurantComponent implements OnInit {
  ads: Restaurant[];
  recommendation: any;
  mall: Mall;

  constructor(private dataService: DataService, private router: Router) { 
    let state = this.router.getCurrentNavigation().extras.state;
    if (state == undefined) {
      this.router.navigate(['/home']);
    } else {
      let data = state.data;
      this.ads = data.ads;
      this.recommendation = data.restaurant;
      this.mall = data.mall;
    }
  }

  ngOnInit(): void {

  }
  
  isEmpty(obj) {
    for(var key in obj) {
      if(obj.hasOwnProperty(key))
        return false;
    }
    return true;
  }
}
