import { Component } from '@angular/core';
import { MeChallengeComponent } from '../me-challenge.component'
import { Challenge } from 'src/app/models';
import { ChallengeService } from 'src/app/challenge.service';
import { ActivatedRoute, Route } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-generated',
  templateUrl: './generated.component.html',
  styleUrls: ['./generated.component.css']
})
export class GeneratedComponent {
  public static Route: Route = {
    path: 'challenge/:id',
    component: GeneratedComponent
  }

  public meChallengeComponent: MeChallengeComponent;
  public challenge: Challenge;
  private challengeService: ChallengeService;


  constructor(private route: ActivatedRoute, challengeService: ChallengeService, meChallengeComponent: MeChallengeComponent, protected http: HttpClient) {
    this.meChallengeComponent = meChallengeComponent
    this.challenge = this.meChallengeComponent.challenge!
    this.challengeService = challengeService
    console.log(this.challenge.id)

    const routeParams = this.route.snapshot.paramMap;
    const idFromRoute = Number(routeParams.get('id'));

    // Find the workshop that correspond with the id provided in route.
    this.challengeService.getChallenge(idFromRoute);
  }
}
