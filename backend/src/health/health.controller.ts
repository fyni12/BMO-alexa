import { Controller, Get } from '@nestjs/common';


@Controller('health')
export class HealthController {
  @Get()
  getHello(): {status: string} {
    return {status: 'ok'};
  }
}