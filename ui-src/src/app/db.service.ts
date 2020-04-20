import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from 'rxjs';
import { Recommendation } from './dto/recommendation';

@Injectable({
    providedIn: 'root'
})
export class DataService {
    private staticUrl: string = "../assets/restaurant.json";

    constructor(private http: HttpClient) { }

    getStaticRecommendation(): Observable<Recommendation> {
        return this.http.get<any>(this.staticUrl);
    }

    getRecommendation(mall: string, cuisine: string, isHalal: boolean, isVeg: boolean, bank: string): Observable<Recommendation> {
        let url = "restaurants/random"
        let postData = { 
            "mall": mall,
            "cuisines": cuisine,
	        "promo_bank": bank,
            "is_hala": isHalal,
            "is_veg": isVeg
        }
        return this.http.post<any>(url, postData);
    }
}