// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

import { CeloPaymentController } from "src/CeloPaymentController.sol";

contract Deploy is Script {
    function run() external returns (CeloPaymentController deployed) {
        address admin = vm.envAddress("ADMIN_WALLET_ADDRESS");
        address operator = vm.envAddress("OPERATOR_WALLET_ADDRESS");

        vm.startBroadcast();
        deployed = new CeloPaymentController(admin, operator);
        vm.stopBroadcast();

        console2.log("Deployed CeloPaymentController at", address(deployed));
    }
}
