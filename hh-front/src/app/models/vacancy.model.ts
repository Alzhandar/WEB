import { Company } from "./company.model";

export class Vacancy {
    id?: number;
    name ?: string;
    description ?: string;
    salary ?: number;
    company?: Company; 
}
