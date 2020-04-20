import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder } from '@angular/forms';
import { SelectModel } from './select.model';
import { Router } from '@angular/router';
import { DataService } from '../db.service';

@Component({
  selector: 'app-selection',
  templateUrl: './selection.component.html',
  styleUrls: ['./selection.component.css']
})
export class SelectionComponent implements OnInit {

  malls: SelectModel[] = [
    { id: 1, name: "313@Somerset" }, 
    { id: 2, name: "Changi City Point" }, 
    { id: 3, name: "NEX" }, 
    { id: 4, name: "Northpoint City" }, 
    { id: 5, name: "Junction 8" }, 
    { id: 6, name: "Junction 10" }, 
    { id: 7, name: "Vivocity" }, 
    { id: 8, name: "Westgate" }
  ];
  cuisines: SelectModel[] = [
    { id: 0, name: "Any" },
    { id: 1, name: "Chinese" }, 
    { id: 2, name: "Fast Food" }, 
    { id: 3, name: "Healthy" }, 
    { id: 4, name: "Indonesian" }, 
    { id: 5, name: "Japanese" }, 
    { id: 6, name: "Korean" }, 
    { id: 7, name: "Seafood" }, 
    { id: 8, name: "Singaporean" }, 
    { id: 9, name: "Thai" }, 
    { id: 10, name: "Vietnamese" }, 
    { id: 11, name: "Western" }
  ];
  banks: SelectModel[] = [
    { id: 0, name: "Any" },
    { id: 1, name: "American Express" }, 
    { id: 2, name: "Citibank" }, 
    { id: 3, name: "DBS" }, 
    { id: 4, name: "HSBC" }, 
    { id: 5, name: "OCBC" }, 
    { id: 6, name: "Maybank" }, 
    { id: 7, name: "Standard Chartered" },
    { id: 8, name: "UOB" }
  ];

  criteriaForm: FormGroup;

  constructor(private fb: FormBuilder, private router: Router, private dataService: DataService) { }

  ngOnInit(): void {
    this.criteriaForm = this.fb.group({
      mall: [this.malls[0].id],
      cuisine: [this.cuisines[0].id],
      isHalal: [false],
      isVeg: [false],
      promo: [this.banks[0].id]
    });
  }

  onSubmit(): void {
    // console.log(this.criteriaForm.value);
    let mallChoice = this.criteriaForm.value.mall;
    let mallName = this.malls[mallChoice-1].name;
    let cuisineChoice = this.criteriaForm.value.cuisine;
    let cuisineName = this.cuisines[cuisineChoice].name;
    if (cuisineName == "Any") {
      cuisineName = "";
    }
    let bankChoice = this.criteriaForm.value.promo;
    let bankName = this.banks[bankChoice].name;
    if (bankName == "Any") {
      bankName = "";
    }
    let halal = this.criteriaForm.value.isHalal;
    let veg = this.criteriaForm.value.isVeg;

    let data = {};
    this.dataService.getRecommendation(mallName, cuisineName, halal, veg, bankName).subscribe({
      next: items => {
        // console.log(items)
        data = items;
        this.router.navigate(['/restaurant'], {state: {data: data}});
      },
      error: error => console.error(error)
    });

    // for dev testing
    // let data = {};
    // this.dataService.getStaticRecommendation().subscribe({
    //   next: items => {
    //     console.log(items)
    //     data = items;
    //     this.router.navigate(['/restaurant'], {state: {data: data}});
    //   },
    //   error: error => console.error(error)
    // });
    
  }
}
