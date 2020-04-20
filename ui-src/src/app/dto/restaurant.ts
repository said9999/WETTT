import { Promotion } from './promotion';

export class Restaurant {
    public cuisine: string;
    public description: string;
    public hours: string;
    public is_halal: boolean;
    public is_veg: boolean;
    public name: string;
    public phone: string;
    public pic_url: string;
    public promotions: Promotion[];
    public unit: string;
    public website: string;
}